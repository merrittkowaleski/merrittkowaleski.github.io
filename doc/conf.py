# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Merritt Kowaleski\'s personal page'
copyright = '2025, Merritt Kowaleski'
author = 'Merritt Kowaleski'
release = '0.2'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# Place rst_epilog at the end of every source file
# line 1: easily write 'ngautonml' with proper formatting
# line 2: allows inline custom html
rst_epilog = """
.. |ngautonml| replace:: ngAuto\\ :sup:`n`\\ ML

.. role:: raw-html(raw)
   :format: html

"""


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
