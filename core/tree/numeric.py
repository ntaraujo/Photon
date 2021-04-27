from methods import Add, Sub, Mul, TrueDiv, Pow, Neg, Pos, Abs, \
    FloorDiv, Mod, DivMod, LShift, RShift, And, Xor, Or, Invert
from node import FuncLike


class Complex(FuncLike):  # C
    __slots__ = ()
    methods = {Add, Sub, Mul, TrueDiv, Pow, Neg, Pos, Abs}
    name = 'complex'


class Float(Complex):  # R
    __slots__ = ()
    methods = {*Complex.methods, FloorDiv, Mod, DivMod}
    name = 'float'


class Exact(Float):  # Q
    __slots__ = ()
    name = 'exact'


class Integer(Float):  # Z
    __slots__ = ()
    methods = {*Exact.methods, LShift, RShift, And, Xor, Or, Invert}
    name = 'int'


class Natural(Integer):  # N
    __slots__ = ()
    name = 'natural'
