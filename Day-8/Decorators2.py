def LoggerFunction(func):
    def wrapper(*args , **kwargs):
        print("Entering "+ func.__name__);
        func(*args , **kwargs);
        print("Exiting "+ func.__name__);
    return wrapper;

@LoggerFunction
def SumOfNumbers(numbers):
    print("Function SumOfNumbers Called....");
    result=0;
    for number in numbers:
        result = result + number;
    return result;

@LoggerFunction
def ProductOfNumbers(numbers):
    print("Function ProductOfNumbers Called....");
    result=1;
    for number in numbers:
        result = result * number;
    return result;

@LoggerFunction
def SumOfNumbers1():
    print("Function SumOfNumbers1 Called....");
    result =50;
    return result;

array = range(1,1000);
SUM = SumOfNumbers(array);
PRODUCT = ProductOfNumbers(array);

