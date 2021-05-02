from control import Raise
from var import Var
total = 0


class NodeBase:
    __slots__ = 'id', 'parent', '__params'

    def __init__(self, parent):
        self.__params = []
        self.parent = parent
        global total
        self.id = total = total + 1

    def __get_params(self):
        return self.get_params()

    def __set_params(self, params):
        self.set_params(params)

    def get_params(self):
        return self.__params

    def set_params(self, params):
        self.__params = params

    def __get_name(self):
        return self.get_name()

    def get_name(self):
        return self.__class__.__name__.lower()

    params = property(__get_params, __set_params)
    name = property(__get_name)
    del __get_params, __set_params, __get_name


class Leaf(NodeBase):
    __slots__ = 'values'

    def __init__(self, value, parent):
        super().__init__(parent)
        self.values = [value]


class Node(NodeBase):
    __slots__ = ()

    def __get_values(self):
        return self.get_values()

    def get_values(self):
        return self.params[-1].values

    values = property(__get_values)
    del __get_values


class VarBase(Node):
    __slots__ = '__var'

    def __init__(self, parent):
        super().__init__(parent)
        self.__var = None

    def get_values(self):
        return self.__var.values


class SetVar(VarBase):
    __slots__ = ()

    def set_params(self, params):
        super().set_params(params)
        block = self.params[1]
        var = params[0].values[-1]
        block.vars[var].setter(self)
        self.__var = block.vars[var]


class GlobalSetVar(VarBase):
    __slots__ = ()


class GetVar(VarBase):
    __slots__ = ()

    def set_params(self, params):
        super().set_params(params)
        block = self.params[1]
        var = params[0].values[-1]
        while True:
            if var in block.vars:
                block.vars[var].getter(self)
                self.__var = block.vars[var]
                break
            else:
                try:
                    block = block.scope_block
                except AttributeError:
                    Raise(NameError, f"name '{var}' is not defined")


class DelVar(VarBase):
    __slots__ = ()

    def set_params(self, params):
        super().set_params(params)
        block = self.params[1]
        var = params[0].values[-1]
        while True:
            if var in block.vars:
                block.vars[var].deleter(self)
                self.__var = block.vars[var]
                break
            else:
                try:
                    block = block.scope_block
                except AttributeError:
                    Raise(NameError, f"name '{var}' is not defined")
