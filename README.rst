========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/jinja2-webpack/badge?version=latest
    :target: http://jinja2-webpack.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/JDeuce/jinja2-webpack.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/JDeuce/python-jinja2-webpack

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/JDeuce/python-jinja2-webpack?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/JDeuce/python-jinja2-webpack

.. |requires| image:: https://requires.io/github/JDeuce/python-jinja2-webpack/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/JDeuce/python-jinja2-webpack/requirements/?branch=master


.. |coveralls| image:: https://coveralls.io/repos/JDeuce/python-jinja2-webpack/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/github/JDeuce/python-jinja2-webpack

.. |codecov| image:: https://codecov.io/github/JDeuce/python-jinja2-webpack/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/JDeuce/python-jinja2-webpack

.. |version| image:: https://img.shields.io/pypi/v/jinja2-webpack.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/jinja2-webpack

.. |commits-since| image:: https://img.shields.io/github/commits-since/JDeuce/python-jinja2-webpack/v0.1.4.svg
    :alt: Commits since latest release
    :target: https://github.com/JDeuce/python-jinja2-webpack/compare/v0.1.4...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/jinja2-webpack.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/jinja2-webpack

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/jinja2-webpack.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/jinja2-webpack

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/jinja2-webpack.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/jinja2-webpack


.. end-badges

Integration of webpack with jinja2

* Free software: BSD license

Description
===========

Plugin for jinja2 which enables you to reference assets generated by webpack in your Jinja2 templates, as well as an optional scan feature which allows you to push references to assets from your Jinja2 templates back into webpack for it to build them.

Installation
============

::

    pip install jinja2-webpack

Documentation
=============

https://jinja2-webpack.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
