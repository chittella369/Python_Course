def outer_func(msg):
    message = msg;
    def inner_func():
        print(message);
    return inner_func();

outer_func("Bangalore");