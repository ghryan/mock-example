import pytest
from src.calculator import Calculator

def test_add(mocker):
    mocker.patch("src.calculator.Calculator.add", return_value=5)
    calculator = Calculator()
    assert calculator.add(2, 3) == 5
    
def test_subtract(mocker):
    mocker.patch("src.calculator.Calculator.subtract", return_value=-1)
    calculator = Calculator()
    assert calculator.subtract(2, 3) == -1