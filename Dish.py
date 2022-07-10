class Dish:
    def __init__(self, name, count_of_components, components):
        self.name = name
        self.components = components
        self.count_of_components = count_of_components

    def __str__(self):
        components_to_str = ''
        for c in self.components:
            components_to_str = components_to_str + c.__str__() + '\n'
        return f'{self.name}\n{self.count_of_components}\n{components_to_str}'
