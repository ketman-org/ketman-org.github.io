import os
import yaml
import markdown
import shutil
from datetime import datetime
from collections import defaultdict
from jinja2 import Environment, FileSystemLoader


def format_date(date_value):
    """Helper function to handle date formatting consistently."""
    if isinstance(date_value, str):
        try:
            return datetime.strptime(date_value, "%Y-%m-%d").strftime("%A, %B %d, %Y")
        except ValueError:
            return date_value
    elif isinstance(date_value, datetime):
        return date_value.strftime("%A, %B %d, %Y")
    return date_value


class NewsletterSiteGenerator:
    def __init__(
        self, content_dir="content", output_dir="output", template_dir="templates"
    ):
        self.content_dir = content_dir
        self.output_dir = output_dir
        self.template_dir = template_dir
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.categories = defaultdict(list)
        self.md = markdown.Markdown(
            extensions=[
                "fenced_code",  # For ``` code blocks
                "codehilite",  # For syntax highlighting
                "tables",  # For tables
                "attr_list",  # For adding classes and IDs
                "meta",  # For metadata
                "footnotes",  # For footnotes
                "toc",  # For table of contents
                "def_list",  # For definition lists
                "smarty",  # For smart quotes
            ],
            extension_configs={
                "codehilite": {
                    "use_pygments": True,
                    "css_class": "codehilite",
                    "linenums": False,
                }
            },
        )

    def setup_directories(self):
        """Create necessary directories if they don't exist."""
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)
        os.makedirs(self.output_dir)
        os.makedirs(os.path.join(self.output_dir, "categories"), exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "static", "css"), exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "static", "js"), exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "static", "images"), exist_ok=True)

    def parse_markdown_file(self, filepath):
        """Parse a markdown file and return front matter and content."""
        with open(filepath, "r") as f:
            content = f.read().split("---\n")
            if len(content) > 2:
                front_matter = yaml.safe_load(content[1])
                self.md.reset()
                main_content = self.md.convert("".join(content[2:]))
                return front_matter, main_content
        return None, None

    def copy_static_files(self):
        """Copy static files from templates to output."""
        static_source = os.path.join(self.template_dir, "static")
        static_dest = os.path.join(self.output_dir, "static")

        if os.path.exists(static_source):
            if os.path.exists(static_dest):
                shutil.rmtree(static_dest)
            shutil.copytree(static_source, static_dest)

    def get_relative_path(self, from_path, to_path):
        """Calculate relative path between two paths."""
        from_parts = from_path.strip("/").split("/")
        to_parts = to_path.strip("/").split("/")

        # Calculate the depth for relative path
        depth = len(from_parts) - 1
        if depth <= 0:
            return to_path

        return "../" * depth + to_path

    def adjust_paths(self, content, current_path):
        """Adjust all paths in content based on current file location."""
        # Handle static paths
        depth = len(current_path.strip("/").split("/")) - 1
        prefix = "../" * depth if depth > 0 else ""

        # Replace paths
        content = content.replace('href="/static/', f'href="{prefix}static/')
        content = content.replace('src="/static/', f'src="{prefix}static/')
        content = content.replace('href="/categories/', f'href="{prefix}categories/')

        # Dynamically handle page paths
        for filename in os.listdir(self.content_dir):
            if filename.endswith(".md"):
                page_name = filename.replace(".md", ".html")
                content = content.replace(
                    f'href="/{page_name}"', f'href="{prefix}{page_name}"'
                )

        # Handle index separately since it might not exist as a file
        content = content.replace('href="/index.html"', f'href="{prefix}index.html"')

        return content

    def load_content(self):
        """Load and parse all markdown files from content directory."""
        articles = []
        pages = {}

        for filename in os.listdir(self.content_dir):
            if not filename.endswith(".md"):
                continue

            filepath = os.path.join(self.content_dir, filename)
            front_matter, main_content = self.parse_markdown_file(filepath)

            if not front_matter:
                continue

            # Determine if this is a page or a post
            is_page = front_matter.get("type", "post") == "page"

            if is_page:
                # Handle page - preserve HTML from markdown
                pages[filename] = {
                    "content": main_content,  # This is now HTML
                    "url": filename.replace(".md", ".html"),
                    "title": front_matter.get("title", ""),
                    **front_matter,
                }
            else:
                # Handle regular posts
                categories = front_matter.get("categories", [])
                if isinstance(categories, str):
                    categories = [categories]
                front_matter["categories"] = categories

                if "image" in front_matter:
                    image_filename = os.path.basename(front_matter["image"])
                    front_matter["image"] = f"static/images/{image_filename}"

                article_data = {
                    "content": main_content,
                    "url": filename.replace(".md", ".html"),
                    "filename": filename,
                    **front_matter,
                }

                if "date" in article_data:
                    article_data["date"] = format_date(article_data["date"])

                articles.append(article_data)

                for category in categories:
                    self.categories[category].append(article_data)

        return (
            sorted(
                articles,
                key=lambda x: (
                    datetime.strptime(x.get("date", ""), "%A, %B %d, %Y")
                    if isinstance(x.get("date"), str)
                    else datetime.now()
                ),
                reverse=True,
            ),
            pages,
        )

    def generate_category_pages(self):
        """Generate individual category pages."""
        category_template = self.env.get_template("category.html")

        for category, articles in self.categories.items():
            sorted_articles = sorted(
                articles,
                key=lambda x: (
                    datetime.strptime(x.get("date", ""), "%A, %B %d, %Y")
                    if isinstance(x.get("date"), str)
                    else datetime.now()
                ),
                reverse=True,
            )

            # Create deep copies of articles to avoid modifying originals
            category_articles = []
            for article in sorted_articles:
                article_copy = article.copy()

                # Fix image paths
                if "image" in article_copy:
                    image_filename = os.path.basename(article_copy["image"])
                    article_copy["image"] = f"../static/images/{image_filename}"

                # Fix content image paths
                if "content" in article_copy:
                    article_copy["content"] = article_copy["content"].replace(
                        'src="static/images/', 'src="../static/images/'
                    )

                category_articles.append(article_copy)

            # Add context for proper path handling in template
            context = {
                "category": category,
                "articles": category_articles,
                "is_category_page": True,  # Flag to indicate we're in a category page
            }

            category_html = category_template.render(**context)

            # Generate the category page path
            category_path = os.path.join(
                self.output_dir, "categories", f"{category.lower()}.html"
            )

            # Use adjust_paths with the relative category path
            category_html = self.adjust_paths(
                category_html, f"categories/{category.lower()}.html"
            )

            os.makedirs(os.path.dirname(category_path), exist_ok=True)
            with open(category_path, "w") as f:
                f.write(category_html)

    def generate_categories_index(self):
        """Generate the categories index page."""
        categories_template = self.env.get_template("categories.html")
        categories_html = categories_template.render(categories=dict(self.categories))

        # Adjust paths for categories index
        categories_html = self.adjust_paths(categories_html, "categories.html")

        with open(os.path.join(self.output_dir, "categories.html"), "w") as f:
            f.write(categories_html)

    def generate_page(self, page_data, template_name):
        """Generate an individual page using specified template."""
        template = self.env.get_template(f"{template_name}.html")
        # The content is already HTML, so we mark it as safe
        page_html = template.render(page=page_data)
        page_html = self.adjust_paths(page_html, page_data["url"])

        output_path = os.path.join(self.output_dir, page_data["url"])
        with open(output_path, "w") as f:
            f.write(page_html)

    def generate_site(self):
        """Generate the complete static site."""
        self.setup_directories()
        articles, pages = self.load_content()

        # Generate index page
        template = self.env.get_template("index.html")
        index_html = template.render(articles=articles)
        index_html = self.adjust_paths(index_html, "index.html")
        with open(os.path.join(self.output_dir, "index.html"), "w") as f:
            f.write(index_html)

        # Generate article pages
        article_template = self.env.get_template("article.html")
        for article in articles:
            if "image" in article:
                article["image"] = self.get_relative_path(
                    article["url"], article["image"]
                )

            article_html = article_template.render(article=article)
            article_html = self.adjust_paths(article_html, article["url"])
            with open(os.path.join(self.output_dir, article["url"]), "w") as f:
                f.write(article_html)

        # Generate individual pages - always use page.html
        for filename, page_data in pages.items():
            self.generate_page(page_data, "page")

        # Generate category pages
        self.generate_category_pages()
        self.generate_categories_index()

        # Copy static files
        self.copy_static_files()


if __name__ == "__main__":
    generator = NewsletterSiteGenerator()
    generator.generate_site()
