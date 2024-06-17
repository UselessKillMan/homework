# def generate_squares(max_number):
#     for number in range(1, max_number + 1):
#         yield number ** 2
#
# for square in generate_squares(10):
#     print(square)

#
# def get_events(num: int):
#     for i in range(num + 1):
#         if i % 2 == 0:
#             yield i
#
# print(get_events(20))


#
# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
#
# for fib_number in fibonacci_generator():
#     print(fib_number)
#     if fib_number > 100:
#         break

#
# import random
# def random_number_generator(min_value, max_value):
#     while True:
#         yield random.randint(min_value, max_value)


#
# def WordGenerator(input_string):
#     for word in input_string.split():
#         yield word


#
# import random
#
# def random_rgb_color_generator(limit):
#     count = 0
#     while count < limit:
#         yield (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#         count += 1
#
# for color in random_rgb_color_generator(10):
#     print(color)



#
# from itertools import permutations
#
# def all_combinations(letters):
#     for i in range(len(letters) + 1):
#         for combination in permutations(letters, i):
#             yield ''.join(combination)
#
# for combo in all_combinations(['a', 'b', 'c']):
#     print(combo)



