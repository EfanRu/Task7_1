class Component:
    def __init__(self, name, count, unit_measurement):
        self.name = name
        self.count = count
        self.unit_measurement = unit_measurement

    def __str__(self):
        return f'{self.name} | {self.count} | {self.unit_measurement}'
