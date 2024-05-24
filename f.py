# def taxi_counter(km, price, add_price) -> str:
#      add_km = int(km - 3) + 1
#      full_price = price + add_km * add_price
#      return full_price
#
# print((taxi_counter(17.5, 2, 0.3)))

# from datetime import datetime
# def logger(func):
#     def wrap(file):
#         print(f"function{func} started{datetime.now()}")
#         print(func(file))
#         print(f"function{func} ended{datetime.now()}")
# @logger
# def get_file(file: str):
#     if not file:
#         return "no File"
#     return file
#




def permission_check(func):
    def wrapper(user_tupe):
        if user_tupe in ('auth_user', 'admin'):
            print("")
            return func(user_tupe)
    return




@permission_check
def hello(user_tupe: str):