# from functools import wraps
#
# def optimize(func):
#     """
#     Декоратор для оптимизации работы функции с помощью кеширования результатов.
#     """
#     cache = {}
#
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         key = str(args) + str(kwargs)
#         if key not in cache:
#             cache[key] = func(*args, **kwargs)
#         return cache[key]
#
#     return wrapper
#
# @optimize
# def slow_function(n):
#     print("Выполнение медленной функции...")
#     import time
#     time.sleep(2)
#     return n * n


# from typing import Any
#
# def check_argument_types(func: Any) -> Any:
#     def decorator(arg: Any) -> Any:
#         if not isinstance(arg, type(func.__annotations__[0])):
#             raise ValueError(f"Argument '{arg}' must be of type '{func.__annotations__[0]}'.")
#         return func(arg)
#     return decorator
#
# @check_argument_types
# def summa(a: int, b: int) -> int:
#     return a + b
