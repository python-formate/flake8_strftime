========
Usage
========

This library provides the Flake8 plugin ``flake8-strftime``  which checks for use of platform specific strftime codes.


Flake8 codes
--------------

.. flake8-codes:: flake8_strftime

	SFT001
	SFT002



Pre-commit hook
----------------

``flake8-strftime`` can also be used as a ``pre-commit`` hook
See `pre-commit <https://github.com/pre-commit/pre-commit>`_ for instructions

Sample ``.pre-commit-config.yaml``:

.. pre-commit:flake8:: 0.3.0
