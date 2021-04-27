class Var:
    __slots__ = 'setters', 'getters', 'deleters'

    def __init__(self, setter):
        self.setters = [setter]
        self.getters = []
        self.deleters = []

    def setter(self, setter):
        self.setters.append(setter)

    def getter(self, getter):
        self.getters.append(getter)

    def deleter(self, deleter):
        self.deleters.append(deleter)

    def __get_values(self):
        values = []
        for setter in self.setters:
            for value in setter.values:
                if value not in values:
                    values.append(value)
        return values

    def values_for_node(self):
        values = {}
        for setter in self.setters:
            values[setter] = setter.values
        return values

    values = property(__get_values)
    del __get_values
