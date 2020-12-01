scroll = [10, "Revolution", 10.5, bool(1)]
print(scroll)
print(type(scroll[0]), type(scroll[1]), type(scroll[2]), type(scroll[3]))

first_answer = input("Введите перевое значение: ")
second_answer = input("Введите второе значение: ")
third_answer = input("Введите третье значение: ")
four_answer = input("Введите четвертое значение: ")
user_scroll = [first_answer, second_answer, third_answer, four_answer]
user_scroll.pop(0)
user_scroll.insert(1, first_answer)
user_scroll.pop(2)
user_scroll.insert(3, third_answer)
print(user_scroll)

user_month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
all_month = dict(January=1, February=2, March=3, April=4, May=5, June=6,
                 July=7, August=8, September=9, October=10, November=11, December=12)
all_seasons = ["Зима", "Весна", "Лето", "Осень"]
if user_month == all_month.get("January"):
    print(all_seasons[0])
elif user_month == all_month.get("February"):
    print(all_seasons[0])
elif user_month == all_month.get("March"):
    print(all_seasons[1])
elif user_month == all_month.get("April"):
    print(all_seasons[1])
elif user_month == all_month.get("May"):
    print(all_seasons[1])
elif user_month == all_month.get("June"):
    print(all_seasons[2])
elif user_month == all_month.get("July"):
    print(all_seasons[2])
elif user_month == all_month.get("August"):
    print(all_seasons[2])
elif user_month == all_month.get("September"):
    print(all_seasons[3])
elif user_month == all_month.get("October"):
    print(all_seasons[3])
elif user_month == all_month.get("November"):
    print(all_seasons[3])
elif user_month == all_month.get("December"):
    print(all_seasons[0])

user_text = input("Введите строку из нескольких слов разделяя слова пробелами: ")
new_user_text = user_text.split()
try_count = 0
while True:
    if try_count >= len(new_user_text):
        break
    else:
        print(try_count + 1, new_user_text[try_count])
    try_count += 1

user_num = int(input("Введите новый элемент рейтинга: "))
constant_list = [7, 5, 3, 3, 2]
attempt_count = 0
while True:
    if user_num == constant_list[attempt_count]:
        constant_list.insert(attempt_count + 1, user_num)
        print(constant_list)
        break
    elif user_num > constant_list[attempt_count]:
        constant_list.insert(attempt_count, user_num)
        print(constant_list)
        break
    elif attempt_count >= len(constant_list) - 1:
        constant_list.insert(attempt_count + 1, user_num)
        print(constant_list)
        break
    attempt_count += 1

first_product_name = input("Введите название первого прдукта: ")
first_product_cost = int(input("Введите стоимость прдукта: "))
first_product_quantity = input("Введите количество прдукта: ")
first_product_unit = input("Введите единицу измерения прдукта: ")
second_product_name = input("Введите название второго прдукта: ")
second_product_cost = int(input("Введите стоимость прдукта: "))
second_product_quantity = input("Введите количество прдукта: ")
second_product_unit = input("Введите единицу измерения прдукта: ")
third_product_name = input("Введите название третьего прдукта: ")
third_product_cost = int(input("Введите стоимость прдукта: "))
third_product_quantity = input("Введите количество прдукта: ")
third_product_unit = input("Введите единицу измерения прдукта: ")
first_product_dictionary = dict(Название=first_product_name, Цена=first_product_cost,
                                Количество=first_product_quantity, Ед=first_product_unit)
second_product_dictionary = dict(Название=second_product_name, Цена=second_product_cost,
                                Количество=second_product_quantity, Ед=second_product_unit)
third_product_dictionary = dict(Название=third_product_name, Цена=third_product_cost,
                                Количество=third_product_quantity, Ед=third_product_unit)
first_product_cortege = tuple(first_product_dictionary)
second_product_cortege = tuple(second_product_dictionary)
third_product_cortege = tuple(third_product_dictionary)
analysis_all_product = dict(Название=[first_product_dictionary.get("Название"),
                                      second_product_dictionary.get("Название"),
                                      third_product_dictionary.get("Название")],
                            Цена=[first_product_dictionary.get("Цена"),
                                  second_product_dictionary.get("Цена"),
                                  third_product_dictionary.get("Цена")],
                            Количество=[first_product_dictionary.get("Количество"),
                                        second_product_dictionary.get("Количество"),
                                        third_product_dictionary.get("Количество")],
                            Ед=[first_product_dictionary.get("Ед"),
                                second_product_dictionary.get("Ед"),
                                third_product_dictionary.get("Ед")])
print("Название", analysis_all_product.get("Название"))
print("Цена", analysis_all_product.get("Цена"))
print("Количество", analysis_all_product.get("Количество"))
print("Ед", analysis_all_product.get("Ед"))
