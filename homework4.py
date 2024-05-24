# string = ["gnu", "fhewi8", "932", "5y3hfh", "854533"]
# b = []
# for i in string:
#     string_list = ''.join(filter(str.isdigit, i))
#     b.append(string_list)
# b = [int(i) for i in string if i.isdigit()]
# print(max(b))



# a = input('chislo:')
# if a.isdigit():
#     print(max(a))
# else:
#  print('error')

#
# student = [{
#     'name': "Hause.M.D.", 'age': 54, 'perfomanse': [5, 5, 5, 5, 5]},
#     {'name': "Rambo", 'age': 26, 'perfomanse': [5, 5, 5, 5, 5]},
#     {'name': "Dean", 'age': 18, 'perfomanse': [5, 5, 5, 5, 5]},
#     {'name': "Cameron", 'age': 32, 'perfomanse': [4, 5, 3, 5, 5]
# }]
# n = len(student)
# for i in range(n):
#     for a in range(0, n - i - 1):
#         if student[a]['age'] < student[a + 1]['age']:
#             student[a], student[a + 1] = student[a + 1], student[a]
# print('list:')
# for students in student:
#  print(students['name'], students['age'], 'age')

#
# a = [25, 6, 3, 19, 99, 24, 56, 78, 90, 4]
# print([x ** 2 for x in a])
# print([x % 11 for x in a])
# print([x for x in a if x % 2 == 0])
# print([x for x in a if len(str(x)) % 2 != 1])
# print([str(x) * 2 for x in a if 10 <= x < 100])
# print([a[x] for x in range(len(a)) if x % 3 != 0])



# a = ['is2 Thi1s T4est 3a"  ->  "Thi1s is2 3a T4est']
# words = a.split()
# numbers = []
# for word in words:
#     num = ''.join(filter(str.isdigit, word))
#     numbers.append((word, int(num)))
    