#####1

#for i in range(1, 11):
 #   print(i)
 #import asyncio

#2
#num = int(input("число: "))
#i = 0
#for i in range(1, num+1):
#       print(i)



#3
#a = 0
#while a < 20:
#    print(a)
#    a += 2
#print("The End:-)")




######4
#a = int(input("Number: "))
#i = 0
#while i < a:
#    print(i)
#    i += 2
#print("Але ОП")



#####5
#for num in range(1, 11):
 #   for num2 in range(1, 11):
  #      print(num * num2)
   # print()

####6
#a = int(input())
#for i in range(1, 11):
   #print(f'{a} * {i} = {a * i}')
# сначала я написал так как снизу, а потом попробовал через ф строки(с ними красивее)
#i = range(1, a)
#for i in range(1, a):
 #   print(a * (i))


#####7
#n = int(input("number: "))
#while 1 < n :
 #   print(f'less {n}')
 #   n -= 1
#print(n)


##########8
#import string
#a = string.ascii_letters
#print(a)



###########9
#word = input()[::-1]
#print(word)


#######10
#word = str(input()).lower()
#a = ""
#for letter in word:
#    if letter != 'a':
#        a += letter
#print(a)



######11
#a = input()
#i = 0
#vowels = "eyuiao"
#counter = 0
#while i <= len(a) - 1:
#   if a[i] in vowels:
#    counter += 1
#   i += 1
#print(counter)

#####12
#words = input().lower()

#count = 0
#for word in words:
#        if 'a' in word:
#            count += 1
#print(count)


###########13

#num1 = int(input("Введите первое число: "))
#num2 = int(input("Введите второе число: "))
#def lcm(a, b):
#    max_num = max(a, b)
#    while True:
 #       if max_num % a == 0 and max_num % b == 0:
  #          return max_num
   #     max_num += 1

#print("Наименьшее общее кратное:", lcm(num1, num2))







#km_h = {'speed_1': 100, 'speed_2': 92, 'speed_3':132, 'speed_4':46}
#b = 1.609
#km_h2 = {k: v * b for (k, v) in km_h.items()}
#print(km_h2)




#a = [4, 2, 3, 4, 5, 5, 5, 4, 4, 5, 5, 2]
#start, end = 0 , 5
#max_five = set()
#for i in range(len(a) - 4):
#    prime = a[start: end]
#    if 2 not in prime or 3 in prime:
#        max_five.add(prime.count(5))
#    start += 1
#    end += 1
#print(max(max_five))









# splitter = "_-"
# array = "the-stealth-warrior"
# array2 = "the_stealth_warrior"
# array3 = "the-stealth_warrior"
# for symbol in splitter:
#      if symbol in array:
#         array = array.replace(symbol, __new=" ")
# print(array)


# a = [4, 4, 1, 5, 7, 9, 12]
# len_a = len(a)
#
# for k in range(len_a):
#     for i in range(len_a - 1):
#         if a[i] > a[i + 1]:
#             a[i], a[i + 1] = a[i + 1], a[i]
# print(a)



# player_1 = input()
# player_2 = input()
#
# vars = ["rock", "scissors", 'paper']
#
# win_dick = {
#     'rock': "scissors",
#     'paper': "paper",
#     'scissors': "rock",
# }
# if win_dick[player_1] == player_2:
#     print('win pl 1')
# elif player_2 == player_1:
#     print('no winner')
# else:
#     print('pl 2 win')

