"""
args：list
kwargs：dict
经常在装饰器中使用
"""

def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# 首先使用 *args
args = ("two", 3, 5)
test_args_kwargs(*args)


# 现在使用 **kwargs:
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)

# 标准参数与*args、**kwargs在使用时的顺序
# some_func(fargs, *args, **kwargs)