# Ketman Website Static Generator

A static site generator for a Ketman website.

## Project Structure
```
your-repository/
├── .github/
│   └── workflows/
│       └── build-deploy.yml
├── content/
│   ├── article1.md
│   └── article2.md
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── article.html
│   └── static/
│       └── css/
│           └── style.css
├── site_generator.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Create a new repository in your organization
   - Go to your GitHub organization
   - Click "New repository"
   - Name it `website` (or your preferred name)
   - Make it public
   - Initialize with a README

2. Clone the repository locally:
```bash
git clone https://github.com/ketman-org/ketman-org.github.io
cd ketman-org.github.io
```

3. Create `requirements.txt`:
```
Jinja2==3.1.4
Markdown==3.7
MarkupSafe==3.0.2
Pygments==2.18.0
PyYAML==6.0.2
```

4. Add all the project files:
   - Copy the provided `site_generator.py`
   - Create the directory structure as shown above
   - Copy the templates and CSS files
   - Add your markdown content files
   - Copy the GitHub workflow file to `.github/workflows/build-deploy.yml`

5. Enable GitHub Pages:
   - Go to your repository settings
   - Navigate to "Pages"
   - Under "Build and deployment":
     - Source: "GitHub Actions"
   - Save the changes

6. Commit and push your changes:
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

## Adding Content

Create markdown files in the `content/` directory with front matter:

```markdown
---
title: Your Article Title
date: 2024-11-01
category: 
   - Technology
   - DPRK
featured: True
image: <image-name>.png
author: John Doe
excerpt: 
   A brief excerpt of the article.
   Or a longer one.
   Or even longer one is fine too.
---

Your article content here in markdown format.
```

## Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run locally:
```bash
python site_generator.py
```

3. Test the output:
   - Open `output/index.html` in your browser

## Deployment

The site will automatically deploy when you push to the main branch. You can view your site at:
`https://your-organization.github.io/website/`

## Customization

- Modify templates in the `templates/` directory
- Update styles in `templates/static/css/style.css`
- Adjust the site generator in `site_generator.py`

## License

MIT License