def outer_func():
    message = "Accenture";    # Free Variable
    def inner_func():
        print(message);
        return message;
    return inner_func;
result1 = outer_func();     # This outer_func() returns line nos 3 , 4, 5 only
print(result1());   

