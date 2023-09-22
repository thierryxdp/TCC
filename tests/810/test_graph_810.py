import pytest
import importlib

test_cases = [
	("frente pra tras", "tras pra frente")
]

@pytest.mark.parametrize("a, output", test_cases)
def test_inverte(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.inverte(a) == output
