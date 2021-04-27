from error import Raise
from var import Var
total = 0


class Node:
    __slots__ = 'id', 'block', '__param', 'line_slice'

    def __init__(self, line_slice, block):
        self.__param = None
        self.block = block
        self.line_slice = line_slice
        global total
        self.id = total = total + 1

    def __get_param(self):
        return self.get_param()

    def __set_param(self, param):
        self.set_param(param)

    def get_param(self):
        return self.__param

    def set_param(self, param):
        self.__param = param

    param = property(__get_param, __set_param)
    del __get_param, __set_param


class Value(Node):
    __slots__ = 'values'

    def __init__(self, value, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.values = [value]


class FuncLike(Node):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __get_values(self):
        return self.get_values()

    def get_values(self):
        return self.param.values

    values = property(__get_values)
    del __get_values


class ClassFuncLike(FuncLike):
    __slots__ = 'parent'

    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent


class Set(FuncLike):
    __slots__ = 'var'

    def __init__(self, var, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.var = var

    def set_param(self, param):
        super().set_param(param)
        if self.var in self.block.vars:
            self.block.vars[self.var].setter(self)
        else:
            self.block.vars[self.var] = Var(self)


class GlobalSet(FuncLike):
    __slots__ = 'var'

    def __init__(self, var, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.var = var

    def set_param(self, param):
        super().set_param(param)
        block = self.block
        while block.block is not None:
            block = block.block
        if self.var in block.vars:
            block.vars[self.var].setter(self)
        else:
            block.vars[self.var] = Var(self)


class Get(FuncLike):
    __slots__ = 'var'

    def __init__(self, var, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.var = var
        block = self.block
        while True:
            if var in block.vars:
                block.vars[var].getter(self)
                self.var = block.vars[var]
                break
            else:
                try:
                    block = block.block
                except AttributeError:
                    Raise(self, NameError, f"name '{var}' is not defined")

    def get_values(self):
        return self.var.values


class Del(Node):
    __slots__ = 'var'

    def __init__(self, var, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.var = var
        block = self.block
        while True:
            if var in block.vars:
                block.vars[var].deleter(self)
                break
            else:
                try:
                    block = block.block
                except AttributeError:
                    Raise(self, NameError, f"name '{var}' is not defined")
