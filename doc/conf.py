import rst_package_refs

# -- Project information
project = "rst-package-refs"
copyright = "2024, Kazuya Takei"
author = "Kazuya Takei"
release = rst_package_refs.__version__

# -- General configuration
extensions = [
    "rst_package_refs.sphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx_tabs.tabs",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output
html_theme = "furo"
html_title = f"{project} v{release}"
html_static_path = ["_static"]

# -- Extension configuration
# For sphinx.ext.intersphinx
intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}


def setup(app):
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
    )
