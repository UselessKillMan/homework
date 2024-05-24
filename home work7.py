# def check_funds(available_funds, shopping_cart):
#
#   available_funds = float(available_funds)
#
#   total_cost = 0
#   for item in shopping_cart:
#     total_cost += item["quantity"] * item["cost"]
#
#     if available_funds >= total_cost:
#      return {
#       "status": "ok",
#       "comment": "Покупки оплачены"
#     }
#   else:
#     amount_needed = total_cost - available_funds
#     return {
#       "status": "error",
#       "comment": f"Недостаточно средств. Внесите {amount_needed:.2f} сумму денег"
#     }




# def create_phone_number(numbers):
#   if len(numbers) != 10:
#     raise ValueError()
#     phone_number = "({}{}{}) {}-{}-{}".format(*numbers)
#   return phone_number





#
#
# from random import randint
# a = list(range(1, 101))
# quess = randint(1, 100)
#
# def binary(num: int, nums: list):
#     start = 0
#     for i in range(1, 8):
#         end = len(nums) // 2
#         print(f"попытка {i}")
#         if num > nums[end]:
#             nums = nums[end:]
#         elif num < nums[end]:
#             nums = nums[:end]
#         else:
#             return num
#























