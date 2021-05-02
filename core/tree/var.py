class Var:
    __slots__ = 'setters', 'getters', 'deleters'

    def __init__(self, *setters):
        self.setters = [*setters]
        self.getters = []
        self.deleters = []

    def setter(self, setter):
        if setter not in self.setters:
            self.setters.append(setter)

    def getter(self, getter):
        if getter not in self.getters:
            self.getters.append(getter)

    def deleter(self, deleter):
        if deleter not in self.deleters:
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


class VarDict(dict):
    def __getitem__(self, item):
        if item not in self:
            self[item] = Var()
        return super().__getitem__(item)
