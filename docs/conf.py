"""Sphinx configuration."""
project = "Test Hm Python"
author = "Cameron Smith"
copyright = "2022, Cameron Smith"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
