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

import this
