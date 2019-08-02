import Calculator;

def test_Add1():
    sum1 = Calculator.Add(10, 20);
    assert sum1 == 30;
def test_Add2():
    sum1 = Calculator.Add(10, -20);
    assert sum1 == -10;
def test_Add3():
    sum1 = Calculator.Add(-10, -20);
    assert sum1 == -30;  
def test_Subtract():
    diff = Calculator.Subtract(20, 4);
    assert diff == 16;