def outer_func(msg):
    def inner_func():
        print(msg);
    return inner_func;

ret_inner_func = outer_func("Bangalore");
ret_inner_func();