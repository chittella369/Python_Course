
def SumOfNumbers(numbers):
    result=0;
    print("Function SumOfNumbers Called....");
    for number in numbers:
        result = result + number;
    return result;


def ProductOfNumbers(numbers):
    print("Function ProductOfNumbers Called....");
    result=1;
    for number in numbers:
        result = result * number;
    return result;

array = range(1,1000);
SumOfNumbers(array);
ProductOfNumbers(array);
