################
flake8_strftime
################

.. start short_desc

**A flake8 plugin which checks for use of platform specific strftime codes.**

.. end short_desc

.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs| |docs_check|
	* - Tests
	  - |travis| |actions_windows| |actions_macos| |coveralls| |codefactor|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Anaconda
	  - |conda-version| |conda-platform|
	* - Activity
	  - |commits-latest| |commits-since| |maintained|
	* - Other
	  - |license| |language| |requires| |pre_commit|

.. |docs| image:: https://img.shields.io/readthedocs/flake8_strftime/latest?logo=read-the-docs
	:target: https://flake8_strftime.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Status

.. |docs_check| image:: https://github.com/domdfcoding/flake8_strftime/workflows/Docs%20Check/badge.svg
	:target: https://github.com/domdfcoding/flake8_strftime/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |travis| image:: https://img.shields.io/travis/com/domdfcoding/flake8_strftime/master?logo=travis
	:target: https://travis-ci.com/domdfcoding/flake8_strftime
	:alt: Travis Build Status

.. |actions_windows| image:: https://github.com/domdfcoding/flake8_strftime/workflows/Windows%20Tests/badge.svg
	:target: https://github.com/domdfcoding/flake8_strftime/actions?query=workflow%3A%22Windows+Tests%22
	:alt: Windows Tests Status

.. |actions_macos| image:: https://github.com/domdfcoding/flake8_strftime/workflows/macOS%20Tests/badge.svg
	:target: https://github.com/domdfcoding/flake8_strftime/actions?query=workflow%3A%22macOS+Tests%22
	:alt: macOS Tests Status

.. |requires| image:: https://requires.io/github/domdfcoding/flake8_strftime/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/flake8_strftime/requirements/?branch=master
	:alt: Requirements Status

.. |coveralls| image:: https://img.shields.io/coveralls/github/domdfcoding/flake8_strftime/master?logo=coveralls
	:target: https://coveralls.io/github/domdfcoding/flake8_strftime?branch=master
	:alt: Coverage

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/flake8_strftime?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/flake8_strftime
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/flake8_strftime
	:target: https://pypi.org/project/flake8_strftime/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/flake8_strftime?logo=python&logoColor=white
	:target: https://pypi.org/project/flake8_strftime/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/flake8_strftime
	:target: https://pypi.org/project/flake8_strftime/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/flake8_strftime
	:target: https://pypi.org/project/flake8_strftime/
	:alt: PyPI - Wheel

.. |conda-version| image:: https://img.shields.io/conda/v/domdfcoding/flake8_strftime?logo=anaconda
	:target: https://anaconda.org/domdfcoding/flake8_strftime
	:alt: Conda - Package Version

.. |conda-platform| image:: https://img.shields.io/conda/pn/domdfcoding/flake8_strftime?label=conda%7Cplatform
	:target: https://anaconda.org/domdfcoding/flake8_strftime
	:alt: Conda - Platform

.. |license| image:: https://img.shields.io/github/license/domdfcoding/flake8_strftime
	:target: https://github.com/domdfcoding/flake8_strftime/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/flake8_strftime
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/flake8_strftime/v0.1.1
	:target: https://github.com/domdfcoding/flake8_strftime/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/flake8_strftime
	:target: https://github.com/domdfcoding/flake8_strftime/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2020
	:alt: Maintenance

.. |pre_commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
	:target: https://github.com/pre-commit/pre-commit
	:alt: pre-commit

.. end shields

Installation
---------------

.. start installation

.. tabs::

	.. tab:: from PyPI

		.. prompt:: bash

			python3 -m pip install flake8_strftime --user

	.. tab:: from Anaconda

		First add the required channels

		.. prompt:: bash

			conda config --add channels http://conda.anaconda.org/domdfcoding
			conda config --add channels http://conda.anaconda.org/conda-forge

		Then install

		.. prompt:: bash

			conda install flake8_strftime

	.. tab:: from GitHub

		.. prompt:: bash

			python3 -m pip install git+https://github.com/domdfcoding/flake8_strftime@master --user

.. end installation


Use as a pre-commit hook
--------------------------

See `pre-commit <https://github.com/pre-commit/pre-commit>`_ for instructions

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://gitlab.com/pycqa/flake8
    rev: 3.8.1
    hooks:
    -   id: flake8
        additional_dependencies: [flake8-strftime==0.1.1]
```


.. toctree::
	:hidden:

	Home<self>

.. toctree::
	:maxdepth: 3
	:caption: Documentation

	codes
	API Reference<docs>
	Source
	Building

.. start links

View the :ref:`Function Index <genindex>` or browse the `Source Code <_modules/index.html>`__.

`Browse the GitHub Repository <https://github.com/domdfcoding/flake8_strftime>`__

.. end links
