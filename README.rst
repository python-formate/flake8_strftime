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
	  - |actions_linux| |actions_windows| |actions_macos| |coveralls|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Anaconda
	  - |conda-version| |conda-platform|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy|
	* - Other
	  - |license| |language| |requires|

.. |docs| image:: https://img.shields.io/readthedocs/flake8_strftime/latest?logo=read-the-docs
	:target: https://flake8_strftime.readthedocs.io/en/latest
	:alt: Documentation Build Status

.. |docs_check| image:: https://github.com/domdfcoding/flake8_strftime/workflows/Docs%20Check/badge.svg
	:target: https://github.com/domdfcoding/flake8_strftime/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |actions_linux| image:: https://github.com/domdfcoding/flake8_strftime/workflows/Linux/badge.svg
	:target: https://github.com/domdfcoding/flake8_strftime/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_windows| image:: https://github.com/domdfcoding/flake8_strftime/workflows/Windows/badge.svg
	:target: https://github.com/domdfcoding/flake8_strftime/actions?query=workflow%3A%22Windows%22
	:alt: Windows Test Status

.. |actions_macos| image:: https://github.com/domdfcoding/flake8_strftime/workflows/macOS/badge.svg
	:target: https://github.com/domdfcoding/flake8_strftime/actions?query=workflow%3A%22macOS%22
	:alt: macOS Test Status

.. |actions_flake8| image:: https://github.com/domdfcoding/flake8_strftime/workflows/Flake8/badge.svg
	:target: https://github.com/domdfcoding/flake8_strftime/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/domdfcoding/flake8_strftime/workflows/mypy/badge.svg
	:target: https://github.com/domdfcoding/flake8_strftime/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

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

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/flake8_strftime/v0.3.2
	:target: https://github.com/domdfcoding/flake8_strftime/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/flake8_strftime
	:target: https://github.com/domdfcoding/flake8_strftime/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2021
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/flake8_strftime
	:target: https://pypi.org/project/flake8_strftime/
	:alt: PyPI - Downloads

.. end shields

|

Installation
--------------

.. start installation

``flake8_strftime`` can be installed from PyPI or Anaconda.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install flake8_strftime

To install with ``conda``:

	* First add the required channels

	.. code-block:: bash

		$ conda config --add channels https://conda.anaconda.org/conda-forge
		$ conda config --add channels https://conda.anaconda.org/domdfcoding

	* Then install

	.. code-block:: bash

		$ conda install flake8_strftime

.. end installation

flake8 codes
--------------

============== ====================================
Code           Description
============== ====================================
STRFTIME001    Linux-specific strftime code used
STRFTIME002    Windows-specific strftime code used
============== ====================================


Use as a pre-commit hook
--------------------------

See `pre-commit <https://github.com/pre-commit/pre-commit>`_ for instructions

Sample ``.pre-commit-config.yaml``:

.. code-block:: yaml

	 - repo: https://gitlab.com/pycqa/flake8
	   rev: 3.8.1
	   hooks:
	    - id: flake8
	      additional_dependencies: [flake8-strftime==0.3.2]
