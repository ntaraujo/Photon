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


class Contains(BinaryOperation):
    __slots__ = ()
    name = '__contains__'


class Hash(UnaryOperation):
    __slots__ = ()
    name = '__hash__'


class Iter(UnaryOperation):
    __slots__ = ()
    name = '__iter__'


class Len(UnaryOperation):
    __slots__ = ()
    name = '__len__'


class Call(BinaryOperation):
    __slots__ = ()
    name = '__call__'


class Next(UnaryOperation):
    __slots__ = ()
    name = '__next__'


class Reversed(UnaryOperation):
    __slots__ = ()
    name = '__reversed__'


class GetItem(BinaryOperation):
    __slots__ = ()
    name = '__getitem__'


class SetItem(BinaryOperation):
    __slots__ = ()
    name = '__setitem__'


class DelItem(BinaryOperation):
    __slots__ = ()
    name = '__delitem__'


class Missing(BinaryOperation):
    __slots__ = ()
    name = '__missing__'


class Bool(UnaryOperation):
    __slots__ = ()
    name = '__bool__'


class New(BinaryOperation):
    __slots__ = ()
    name = '__new__'


class Init(BinaryOperation):
    __slots__ = ()
    name = '__init__'


class Del(UnaryOperation):
    __slots__ = ()
    name = '__del__'


class Repr(UnaryOperation):
    __slots__ = ()
    name = '__repr__'


class Str(UnaryOperation):
    __slots__ = ()
    name = '__str__'


class Bytes(UnaryOperation):
    __slots__ = ()
    name = '__bytes__'


class Format(UnaryOperation):
    __slots__ = ()
    name = '__format__'


class Lt(BinaryOperation):
    __slots__ = ()
    name = '__lt__'


class Le(BinaryOperation):
    __slots__ = ()
    name = '__le__'


class Eq(BinaryOperation):
    __slots__ = ()
    name = '__eq__'


class Ne(BinaryOperation):
    __slots__ = ()
    name = '__ne__'


class Gt(BinaryOperation):
    __slots__ = ()
    name = '__gt__'


class Ge(BinaryOperation):
    __slots__ = ()
    name = '__ge__'


class GetAttr(BinaryOperation):
    __slots__ = ()
    name = '__getattr__'


class GetAttribute(BinaryOperation):
    __slots__ = ()
    name = '__getattribute__'


class Dir(BinaryOperation):
    __slots__ = ()
    name = '__dir__'


class Get(BinaryOperation):
    __slots__ = ()
    name = '__get__'


class Set(BinaryOperation):
    __slots__ = ()
    name = '__set__'


class Delete(BinaryOperation):
    __slots__ = ()
    name = '__delete__'


class SetName(BinaryOperation):
    __slots__ = ()
    name = '__set_name__'


class InstanceCheck(BinaryOperation):
    __slots__ = ()
    name = '__instancecheck__'


class SubClassCheck(BinaryOperation):
    __slots__ = ()
    name = '__subclasscheck__'


class LengthHint(BinaryOperation):
    __slots__ = ()
    name = '__length_hint__'


class Raw(UnaryOperation):
    __slots__ = ()
    name = '__raw__'
