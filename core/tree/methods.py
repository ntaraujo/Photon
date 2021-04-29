from itertools import product
from node import Node


class MethodBase(Node):
    __slots__ = ()

    def get_name(self):
        return f'__{super().get_name()}__'


class BinaryOperation(MethodBase):
    __slots__ = ()

    def get_values(self):
        this, other = self.params
        operator_format = f'{{}}.{self.name}({{}})'.format

        return list({operator_format(*values) for values in product(this.values, other.values)})


class Add(BinaryOperation):
    __slots__ = ()


class Sub(BinaryOperation):
    __slots__ = ()


class Mul(BinaryOperation):
    __slots__ = ()


class MatMul(BinaryOperation):
    __slots__ = ()


class TrueDiv(BinaryOperation):
    __slots__ = ()


class FloorDiv(BinaryOperation):
    __slots__ = ()


class Mod(BinaryOperation):
    __slots__ = ()


class DivMod(BinaryOperation):
    __slots__ = ()


class Pow(BinaryOperation):
    __slots__ = ()


class LShift(BinaryOperation):
    __slots__ = ()


class RShift(BinaryOperation):
    __slots__ = ()


class And(BinaryOperation):
    __slots__ = ()


class Xor(BinaryOperation):
    __slots__ = ()


class Or(BinaryOperation):
    __slots__ = ()


class UnaryOperation(MethodBase):
    __slots__ = ()

    def get_values(self):
        operator_format = f'{{}}{self.name}()'.format
        return list({operator_format(value) for value in self.params[0].values})


class Pos(UnaryOperation):
    __slots__ = ()


class Neg(UnaryOperation):
    __slots__ = ()


class Abs(UnaryOperation):
    __slots__ = ()


class Invert(UnaryOperation):
    __slots__ = ()


class Contains(BinaryOperation):
    __slots__ = ()


class Hash(UnaryOperation):
    __slots__ = ()


class Iter(UnaryOperation):
    __slots__ = ()


class Len(UnaryOperation):
    __slots__ = ()


class Call(BinaryOperation):
    __slots__ = ()


class Next(UnaryOperation):
    __slots__ = ()


class Reversed(UnaryOperation):
    __slots__ = ()


class GetItem(BinaryOperation):
    __slots__ = ()


class SetItem(BinaryOperation):
    __slots__ = ()


class DelItem(BinaryOperation):
    __slots__ = ()


class Missing(BinaryOperation):
    __slots__ = ()


class Bool(UnaryOperation):
    __slots__ = ()


class New(BinaryOperation):
    __slots__ = ()


class Init(BinaryOperation):
    __slots__ = ()


class Del(UnaryOperation):
    __slots__ = ()


class Repr(UnaryOperation):
    __slots__ = ()


class Str(UnaryOperation):
    __slots__ = ()


class Bytes(UnaryOperation):
    __slots__ = ()


class Format(UnaryOperation):
    __slots__ = ()


class Lt(BinaryOperation):
    __slots__ = ()


class Le(BinaryOperation):
    __slots__ = ()


class Eq(BinaryOperation):
    __slots__ = ()


class Ne(BinaryOperation):
    __slots__ = ()


class Gt(BinaryOperation):
    __slots__ = ()


class Ge(BinaryOperation):
    __slots__ = ()


class GetAttr(BinaryOperation):
    __slots__ = ()


class GetAttribute(BinaryOperation):
    __slots__ = ()


class Dir(BinaryOperation):
    __slots__ = ()


class Get(BinaryOperation):
    __slots__ = ()


class Set(BinaryOperation):
    __slots__ = ()


class Delete(BinaryOperation):
    __slots__ = ()


class SetName(BinaryOperation):
    __slots__ = ()
    name = '__set_name__'


class InstanceCheck(BinaryOperation):
    __slots__ = ()


class SubClassCheck(BinaryOperation):
    __slots__ = ()


class LengthHint(BinaryOperation):
    __slots__ = ()
    name = '__length_hint__'


class Raw(UnaryOperation):
    __slots__ = ()
