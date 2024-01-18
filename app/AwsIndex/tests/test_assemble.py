import pytest

def throw_error():
    raise SystemExit(1)

def test_throw_error():
    with pytest.raises(SystemExit):
        throw_error()

        