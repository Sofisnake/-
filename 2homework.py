from pprint import pprint
with open('recipes.txt', 'rt', encoding="UTF-8") as file:
    cook_book = {}
    for line in file:
        name_cook = line.strip() # первая строка с удалением переноса
        sum_ingr = file.readline() # вторая строка с кол-во ингридиентов
        ingredeient =[]
        for _ in range(int(sum_ingr)):
            ingredeient_name, quantity, measure = file.readline().strip().split(' | ')
            ingredeient.append({
                'ingredeient_name': ingredeient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[name_cook] = ingredeient
# pprint(cook_book, sort_dicts=False)

def get_shop_list_by_dishes(dishes: list, person_count: int):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for ingr in cook_book[dish]:
                ingr['quantity'] = int(ingr['quantity'])
                ingr['quantity'] *= (person_count)
                happy_dict = ingr.pop('ingredeient_name')
                result[happy_dict] = ingr
    return result

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))



