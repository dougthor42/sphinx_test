# sphinx_test
Playing around with Sphinx and trying to get docs built


# Steps:

1. sphinx-quickstart

  - path = .\doc
  - make sure to say yes to autodoc extension

2. add ``'sphinx.ext.napoleon'`` to extensions in doc\conf.py
3. Change html_theme to ``'sphinx_rtd_theme'`` in doc\conf.py
4. Run sphinx-apidoc -f -o doc sphinx_test from trunk\sphinx_test
5. ``cd doc``
6. ``make.bat html``
7. View html at trunk\sphinx_test\doc\_build\html