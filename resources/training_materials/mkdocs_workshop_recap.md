# MkDocs Workshop Recap

**Date:** 8 December, 2023  
**Workshop Leader:** Kalle Westerling  
**Recording:** https://thealanturininstitute.sharepoint.com/:v:/s/RAM/EbXiTi9bFd5Ol-nJLTapQGMBTwz5nK01QzzXVNWwz5jXdg?e=vIVb6W

---

## Introduction
The workshop began with an overview of MkDocs, comparing it with Sphinx and JupyterBook, and discussing its relationship with static site generators.

### Comparison with Sphinx and JupyterBook
- **MkDocs:** [MkDocs Official Site](https://www.mkdocs.org/)
- **Sphinx:** [Sphinx Documentation](https://www.sphinx-doc.org/en/master/)
- **JupyterBook:** [JupyterBook Official Site](https://jupyterbook.org) (built on Sphinx: [JupyterBook and Sphinx](https://jupyterbook.org/en/stable/sphinx/index.html))

### Static Site Generators
We explored similarities and differences between MkDocs and static site generators:
- [Jekyll](https://jekyllrb.com/)
- [Hugo Quick Start Guide](https://gohugo.io/getting-started/quick-start/)

## MkDocs Setup and Usage
We learned how to set up a basic MkDocs site and understood the difference between `mkdocs serve` and `mkdocs build`.

### Setting Up MkDocs
Commands used for setting up:

```
$ mkdocs new test-mkdocs
$ cd test-mkdocs
$ code .
$ mkdocs serve
```

*Note: The `code` command might require [installing VSCode in your PATH](https://safjan.com/add-vscode-to-path/).

### Understanding `mkdocs serve` vs `mkdocs build`
- `mkdocs serve`: For live development and preview. Open https://localhost:8000 in your browser and it'll automatically reload when you update your local site.
- `mkdocs build`: Generates static site output in the `site` folder, not updated in serve mode.

## Configuration and Theming
We delved into configuring navigation and applying themes in MkDocs.

### Navigation Setup
- Setting up navigation in `mkdocs.yml`: [MkDocs Navigation Configuration](https://www.mkdocs.org/user-guide/configuration/#nav).
- MkDocs creates a structure from your files, but `nav` instruction can override this.

### Themes and Appearance
- Experimented with `theme: readthedocs` and the [Material for MkDocs theme](https://squidfunk.github.io/mkdocs-material/).
- Discussed the need to install themes before adding to the configuration.
- Explored available themes: [MkDocs Themes Catalog](github.com/mkdocs/catalog#-theming).

### Managing Requirements
- Importance of using virtual or conda environments.
- Brief discussion on avoiding "requirement hell" with Anaconda. (Ultimately, Alden uninstalled Anaconda and reinstalled [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/) instead.)

## GitHub Integration and Plugins
Together, we learned to deploy their MkDocs site to GitHub and utilize plugins.

### Deploying to GitHub
- Using `mkdocs gh-deploy` to publish to GitHub Pages ([GitHub Pages Documentation](https://pages.github.com/)).

### Using Plugins
- Demonstration of the [`mkdocs-charts-plugin`](https://github.com/timvink/mkdocs-charts-plugin) for interactive charts.

---

Sophie provided valuable insights on technical best practices throughout the workshop, emphasizing the importance of working within virtual or conda environments to manage dependencies effectively.
