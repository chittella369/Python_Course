import time
def timerFunction(func):
    def wrapper(*args , **kwargs):
        start = time.time();
        result = func(*args , **kwargs);    # any function (argument)
        end = time.time();
        print(func.__name__ + " took " + str((end-start)*1000) + " Milli Seconds");
        return result;
    return wrapper;


@timerFunction
def SumOfNumbers(numbers):
    print("Function SumOfNumbers Called....");
    result=0;
    for number in numbers:
        result = result + number;
    return result;

@timerFunction
def ProductOfNumbers(numbers):
    print("Function ProductOfNumbers Called....");
    result=1;
    for number in numbers:
        result = result * number;
    return result;


@timerFunction
def SumOfNumbers1(numbers):
    print("Function SumOfNumbers1 Called....");
    result=0;
    for number in numbers:
        result = result + number;
    return result;
array = range(1,1000);
SUM = SumOfNumbers(array);
PRODUCT = ProductOfNumbers(array);
SUM = SumOfNumbers1(array);
