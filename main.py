from Component import Component
from Dish import Dish

if __name__ == '__main__':
    dish_list = []
    with open('cookBook.txt', 'rt', encoding='utf8') as f:
        while f.readable():
            dish_name = f.readline().strip()
            if not dish_name:
                break
            a = f.readline().strip()
            count_of_components = int(a)
            componentsArr = []
            for i in range(count_of_components):
                components_line = f.readline().split('|')
                components_name = components_line[0].strip()
                components_count = components_line[1].strip()
                components_unit = components_line[2].strip()
                componentsArr.append(Component(components_name, components_count, components_unit))
            dish = Dish(dish_name, count_of_components, componentsArr)
            if f.readable():
                f.readline()
            dish_list.append(dish)
    for d in dish_list:
        print(d)
