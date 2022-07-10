cook_book = {}


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for component in cook_book.get(dish):
            ingredient_name = component.get('ingredient_name')
            if ingredient_name in shop_list.keys():
                quantity = int(shop_list.get(ingredient_name)) + int(component.get('quantity'))
            else:
                quantity = int(component.get('quantity'))
            shop_list.update({ingredient_name: {'measure': component.get('measure'), 'quantity': quantity}})
    for component in shop_list.keys():
        shop_list.update({component:
                              {'measure': shop_list.get(component).get('measure'),
                               'quantity': shop_list.get(component).get('quantity') * person_count}})
    return shop_list


if __name__ == '__main__':
    with open('cookBook.txt', 'rt', encoding='utf8') as f:
        while f.readable():
            dish_name = f.readline().strip()
            if not dish_name:
                break
            count_of_components = int(f.readline().strip())
            componentsArr = []
            for i in range(count_of_components):
                components_line = f.readline().split('|')
                components_name = components_line[0].strip()
                components_count = components_line[1].strip()
                components_unit = components_line[2].strip()
                componentsArr.append(
                    {'ingredient_name': components_name, 'quantity': components_count, 'measure': components_unit})
            cook_book.update({dish_name: componentsArr})
            if f.readable():
                f.readline()
    # print(cook_book)
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
