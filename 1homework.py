from pprint import pprint
with open('recipes.txt', 'rt', encoding="UTF-8") as file:
    cook_book = {}
    for line in file:
        name_cook = line.strip() # первая строка с удалением переноса
        sum_ingr = int(file.readline().strip()) # вторая строка с кол-во ингридиентов
        ingredeient =[]
        for _ in range(sum_ingr):
            ingredeient_name, quantity, measure = file.readline().strip().split(' | ')
            ingredeient.append({
                'ingredeient_name': ingredeient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[name_cook] = ingredeient
pprint(cook_book, sort_dicts=False)





# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }