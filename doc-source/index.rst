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
	  - |travis| |actions_windows| |actions_macos| |coveralls| |codefactor| |pre_commit_ci|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Anaconda
	  - |conda-version| |conda-platform|
	* - Activity
	  - |commits-latest| |commits-since| |maintained|
	* - Other
	  - |license| |language| |requires| |pre_commit|

.. |docs| rtfd-shield::
	:project: flake8_strftime
	:alt: Documentation Build Status

.. |docs_check| actions-shield::
	:workflow: Docs Check
	:alt: Docs Check Status

.. |travis| actions-shield::
	:workflow: Linux Tests
	:alt: Linux Test Status

.. |actions_windows| actions-shield::
	:workflow: Windows Tests
	:alt: Windows Test Status

.. |actions_macos| actions-shield::
	:workflow: macOS Tests
	:alt: macOS Test Status

.. |requires| requires-io-shield::
	:alt: Requirements Status

.. |coveralls| coveralls-shield::
	:alt: Coverage

.. |codefactor| codefactor-shield::
	:alt: CodeFactor Grade

.. |pypi-version| pypi-shield::
	:project: flake8_strftime
	:version:
	:alt: PyPI - Package Version

.. |supported-versions| pypi-shield::
	:project: flake8_strftime
	:py-versions:
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| pypi-shield::
	:project: flake8_strftime
	:implementations:
	:alt: PyPI - Supported Implementations

.. |wheel| pypi-shield::
	:project: flake8_strftime
	:wheel:
	:alt: PyPI - Wheel

.. |conda-version| image:: https://img.shields.io/conda/v/domdfcoding/flake8_strftime?logo=anaconda
	:target: https://anaconda.org/domdfcoding/flake8_strftime
	:alt: Conda - Package Version

.. |conda-platform| image:: https://img.shields.io/conda/pn/domdfcoding/flake8_strftime?label=conda%7Cplatform
	:target: https://anaconda.org/domdfcoding/flake8_strftime
	:alt: Conda - Platform

.. |license| github-shield::
	:license:
	:alt: License

.. |language| github-shield::
	:top-language:
	:alt: GitHub top language

.. |commits-since| github-shield::
	:commits-since: v0.2.0
	:alt: GitHub commits since tagged version

.. |commits-latest| github-shield::
	:last-commit:
	:alt: GitHub last commit

.. |maintained| maintained-shield:: 2020
	:alt: Maintenance

.. |pre_commit| pre-commit-shield::
	:alt: pre-commit

.. |pre_commit_ci| pre-commit-ci-shield::
	:alt: pre-commit.ci status

.. end shields

Installation
---------------

.. start installation

.. installation:: flake8_strftime
	:pypi:
	:github:
	:anaconda:
	:conda-channels: domdfcoding, conda-forge

.. end installation


Use as a pre-commit hook
--------------------------

See `pre-commit <https://github.com/pre-commit/pre-commit>`_ for instructions

Sample ``.pre-commit-config.yaml``:

.. pre-commit:flake8:: 0.2.0


.. toctree::
	:hidden:

	Home<self>

.. toctree::
	:maxdepth: 3
	:caption: Documentation

	codes
	API Reference<docs>


.. toctree::
	:maxdepth: 3
	:caption: Contributing

	contributing
	Source

.. start links

View the :ref:`Function Index <genindex>` or browse the `Source Code <_modules/index.html>`__.

`Browse the GitHub Repository <https://github.com/domdfcoding/flake8_strftime>`__

.. end links
