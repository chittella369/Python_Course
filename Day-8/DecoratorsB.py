import time
def SumOfNumbers(numbers):
    print("Function SumOfNumbers Called....");
    start = time.time();
    result=0;
    for number in numbers:
        result = result + number;
    end = time.time();
    print(__name__ + " took " + str((end-start)*1000) + " Milli Seconds");
    return result;

def ProductOfNumbers(numbers):
    print("Function ProductOfNumbers Called....");
    start = time.time();
    result=1;
    for number in numbers:
        result = result * number;
    end = time.time();
    print(__name__ + " took " + str((end-start)*1000) + " Milli Seconds");
    return result;

array = range(1,1000);
SUM = SumOfNumbers(array);
PRODUCT = ProductOfNumbers(array);

