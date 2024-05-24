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




#character = input("Введите букву английского алфавита: ")

#match character.lower():
#    case 'y'| 'a'| 'e'| 'i'| 'o'| 'u':
#        print(f" '{character}' является гласной")
#    case _ if 'a' <= character.lower() <= 'z':
#        print(f" '{character}' является согласной")
#    case _:
#        print(f" '{character}' не является буквой английского алфавита")

##########2
#def check(day):
  #  day = day.lower()
  #  match day:
  #      case  "monday"| "tuesday"| "wednesday"| "thursday"| "friday":
  #          print( "Это рабочий день.")
  #      case "saturday", "sunday":
  #          print( "Это выходной день.")
  #      case _:
 #           print( "Неверный день недели")


#def fruit_color(fruit):
#     match fruit:
#        case "яблоко":
#            print( "красного, зеленого или желтого цвета")
#        case "банан":
#            print( "желтого цвета")
#        case "апельсин":
#            print( "оранжевого цвета")
#        case _:
#            print( "неизвестен")
#
#fruit = input("Введите название фрукта: ")
#print(fruit_color(fruit))



################
#def student_performance(grade):
#     match grade:
#        case 5:
#            return "Отлично"
#        case 4:
#            return "Хорошо"
 ###       case 3:
#            return "по сути норм"
#        case 2| 1:
#            return "Херово"
#        case _:
#            return "Не поддерживается"
#
#grade = int(input("Введите оценку студента (от 1 до 5): "))
#print("Успеваемость студента:", student_performance(grade))
