import ast

import pytest

from flake8_strftime import Plugin


def results(s):
    return {'{}:{}: {}'.format(*r) for r in Plugin(ast.parse(s)).run()}





def test_linux_specific():
    assert results('print(f"{now:%Y/%-m/%-d %H:%M}")') == {
            '1:9: STRFTIME001 Linux-specific strftime code used.',
            '1:13: STRFTIME001 Linux-specific strftime code used.',
            }

    assert results('print(now.strftime("%Y/%-m/%-d %H:%M"))') == {
            '1:22: STRFTIME001 Linux-specific strftime code used.',
            '1:26: STRFTIME001 Linux-specific strftime code used.',
            }


def test_windows_specific():
    assert results('print(f"{now:%Y/%#m/%#d %H:%M}")') == {
            '1:9: STRFTIME002 Windows-specific strftime code used.',
            '1:13: STRFTIME002 Windows-specific strftime code used.',
            }

    assert results('print(now.strftime("%Y/%#m/%#d %H:%M"))') == {
            '1:22: STRFTIME002 Windows-specific strftime code used.',
            '1:26: STRFTIME002 Windows-specific strftime code used.',
            }

