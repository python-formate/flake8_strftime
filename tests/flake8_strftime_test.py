# stdlib
import ast
from typing import Set

# 3rd party
import pytest

# this package
from flake8_strftime import Plugin


def results(s: str) -> Set[str]:
	return {"{}:{}: {}".format(*r) for r in Plugin(ast.parse(s)).run()}


def test_linux_specific():
	assert results('print(f"{now:%Y/%-m/%-d %H:%M}")') == {  # noqa: STRFTIME001
		"1:9: STRFTIME001 Linux-specific strftime code used.",
		"1:13: STRFTIME001 Linux-specific strftime code used.",
		}

	assert results('print(now.strftime("%Y/%-m/%-d %H:%M"))') == {  # noqa: STRFTIME001
		"1:22: STRFTIME001 Linux-specific strftime code used.",
		"1:26: STRFTIME001 Linux-specific strftime code used.",
		}


def test_windows_specific():
	assert results('print(f"{now:%Y/%#m/%#d %H:%M}")') == {  # noqa: STRFTIME002
		"1:9: STRFTIME002 Windows-specific strftime code used.",
		"1:13: STRFTIME002 Windows-specific strftime code used.",
		}

	assert results('print(now.strftime("%Y/%#m/%#d %H:%M"))') == {  # noqa: STRFTIME002
		"1:22: STRFTIME002 Windows-specific strftime code used.",
		"1:26: STRFTIME002 Windows-specific strftime code used.",
		}


@pytest.mark.parametrize(
		"source",
		[
				"test_none = None",
				"test_ellipsis = ...",
				"test_int = 42",
				"test_float = 1.0",
				"test_list = [1, 2, 3]",
				"test_tuple = (1, 2, 3)",
				"test_set = {1, 2, 3}",
				'test_dict = {"a": 1, "b": 2, "c": 3}',
				]
		)
def test_issue_10(source: str):
	# https://github.com/domdfcoding/flake8_strftime/issues/10
	# This shouldn't raise an exception
	assert not list(Plugin(ast.parse(source)).run())
