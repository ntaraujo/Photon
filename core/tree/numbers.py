from methods import Add, Sub, Mul, TrueDiv, Pow, Neg, Pos, Abs, FloorDiv, Mod, \
    DivMod, LShift, RShift, And, Xor, Or, Invert, Lt, Le, Eq, Ne, Gt, Ge
from node import Node


class Complex(Node):  # C
    __slots__ = ()
    methods = {Add, Sub, Mul, TrueDiv, Pow, Neg, Pos, Abs, Eq, Ne}


class Float(Complex):  # R
    __slots__ = ()
    methods = {*Complex.methods, FloorDiv, Mod, DivMod, Lt, Le, Gt, Ge}


class Exact(Float):  # Q
    __slots__ = ()


class Integer(Float):  # Z
    __slots__ = ()
    methods = {*Exact.methods, LShift, RShift, And, Xor, Or, Invert}
    name = 'int'


class Natural(Integer):  # N
    __slots__ = ()
