# def numbers(nums):
#   return list(filter(lambda x: x % 2 == 0, nums))



# def sum_numbers(a, b):
#     return lambda: a + b


# def long_strings(strings):
#     return list(filter(lambda x: len(x) > 3, strings))


# def squar(nums):
# return list(map(lambda x: x ** 2, nums))


#
# def words_starting_with_a(words):
#     return list(filter(lambda x: x[0].lower() == "a", words))


#
# def numbers(nums):
#     return list(filter(lambda x: x > 10, nums))


#
# def get_strings(strings):
#     return list(filter(lambda x: x.isupper(), strings))



# def numbers3(nums):
#     return list(filter(lambda x: x % 3 == 0, nums))



# def numbers_in_range(nums):
#     return list(filter(lambda x: 5 <= x <= 10, nums))




# def ending_o(strings):
#     return list(filter(lambda x: x.endswith("о"), strings))

# from random import randint, choice
#
# names= ["Walter", "Jessie", "John", "Gustawo",
#         "Thomas", "Frodo", "Bilbo", "Sam", "Dean"]
# names_counter = len(names) - 1
# surenames = ["White", "Adisson", "Shelby", "Ford", "Winchester"]
# surname_counter = len(surenames) - 1
# def gen_customer() -> dict:
#     customer = {
#         "name": choice(names),
#         "surename": choice(surenames),
#         "accaunt":f"{randint(50000, 200000)}$"
#         }
#
#     return customer
# print(gen_customer())
#
# def gen_house(count: int) -> list[dict]:
#     house_list = []
#     for _ in range(count):
#         house = {
#         "price": f"{randint(50, 200000)}$",
#         "square": f"{randint(50, 100)}m2"
#         }
#         house_list.append(house)
#     return house_list
#
#
# def square_to_int (square: int) -> int:
#     return int(square[:-2])
#
#
# def prise_to_int(price: int) -> int:
#     return int(price[:-1])
#
# def get_recommend(customer, house_list) -> dict:
#     customer_account = prise_to_int((customer['accaunt']))
#     res = list(filter(lambda x: prise_to_int(x["price"]) <= customer_account,  house_list))
#     res.sort(key=lambda x: square_to_int(x["square"]), reverse=True)
#     return f"{customer}\n{res}"
#
# print(get_recommend(customer=gen_customer(), house_list=gen_house(20)))



