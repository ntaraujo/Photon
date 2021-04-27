from node import ClassFuncLike, FuncLike


class BinaryOperation(ClassFuncLike):
    __slots__ = ()
    name = '__add__'

    def get_values(self):
        values = []

        param_values = self.param.values
        operator_format = f'{{}}.{self.name}({{}})'.format
        for value_a in self.parent.values:
            for value_b in param_values:
                fmt = operator_format(value_a, value_b)
                if fmt not in values:
                    values.append(fmt)
        return values


class Add(BinaryOperation):
    __slots__ = ()
    name = '__add__'


class Sub(BinaryOperation):
    __slots__ = ()
    name = '__sub__'


class Mul(BinaryOperation):
    __slots__ = ()
    name = '__mul__'


class MatMul(BinaryOperation):
    __slots__ = ()
    name = '__matmul__'


class TrueDiv(BinaryOperation):
    __slots__ = ()
    name = '__truediv__'


class FloorDiv(BinaryOperation):
    __slots__ = ()
    name = '__floordiv__'


class Mod(BinaryOperation):
    __slots__ = ()
    name = '__mod__'


class DivMod(BinaryOperation):
    __slots__ = ()
    name = '__divmod__'


class Pow(BinaryOperation):
    __slots__ = ()
    name = '__pow__'


class LShift(BinaryOperation):
    __slots__ = ()
    name = '__lshift__'


class RShift(BinaryOperation):
    __slots__ = ()
    name = '__rshift__'


class And(BinaryOperation):
    __slots__ = ()
    name = '__and__'


class Xor(BinaryOperation):
    __slots__ = ()
    name = '__xor__'


class Or(BinaryOperation):
    __slots__ = ()
    name = '__or__'


class UnaryOperation(FuncLike):
    __slots__ = ()
    name = '__pos__'

    def get_values(self):
        values = []

        operator_format = f'{self.name}({{}})'.format
        for value in self.param.values:
            fmt = operator_format(value)
            if fmt not in values:
                values.append(fmt)
        return values


class Pos(UnaryOperation):
    __slots__ = ()
    name = '__pos__'


class Neg(UnaryOperation):
    __slots__ = ()
    name = '__neg__'


class Abs(UnaryOperation):
    __slots__ = ()
    name = '__abs__'


class Invert(UnaryOperation):
    __slots__ = ()
    name = '__invert__'
