#students = [
 #   {"name": "Ivan", "age": 15, "mark_list": [7, 8, 5, 4, 9]},
  #  {"name": "Alexey", "age": 14, "mark_list": [6, 4, 3, 2, 7]},
   # {"name": "Maria", "age": 16, "mark_list": [9, 9, 8, 7, 8]},
    #{"name": "alex" , "age": 12, "mark_list": [7,4,9,10,9,6]}
#]

#filter = [student for student in students if sum(student["mark_list"]) / len(student["mark_list"]) > 7.0]

#print("Студенты с средним баллом выше 7.0:")
#for student in filter:
 #   print("Имя:", student["name"])
  #  print("Возраст:", student["age"])
   # print("Средний балл:", sum(student["mark_list"]) / len(student["mark_list"]))
    #print()


##############
#a = int(input())
#b = int(input())
#squar = [x**2 for x in range(a, b + 1)]
#print("Список квадратов чисел от", a, "до", b, ":", squar)


###########
#a = int(input())
#b = int(input())
#numbers = [N for N in range(a, b+1) if N % 2 == 0]
#print(numbers)


###########
#array = input("Введите строку: ")
#vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
#strings = [''.join(char for char in word if char in vowels) for word in array.split()]
#print(strings)






################
#numbers = [num for num in range(1, 101) if num % 3 == 0 and num % 5 == 0]
#print(numbers)


#list = [[i for i in range(l, l+4)] for l in range(1, 10, 4)]
#print(list)
