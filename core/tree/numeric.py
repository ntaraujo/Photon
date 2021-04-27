from methods import Add, Sub, Mul, TrueDiv, Pow, Neg, Pos, Abs, \
    FloorDiv, Mod, DivMod, LShift, RShift, And, Xor, Or, Invert
from node import FuncLike


class Complex(FuncLike):
    __slots__ = ()
    methods = {Add, Sub, Mul, TrueDiv, Pow, Neg, Pos, Abs}


class Exact(Complex):
    __slots__ = ()
    methods = {*Complex.methods, FloorDiv, Mod, DivMod}


class Integer(Exact):
    __slots__ = ()
    methods = {*Exact.methods, LShift, RShift, And, Xor, Or, Invert}


class Float(Exact):
    __slots__ = ()


class Natural(Integer):
    __slots__ = ()
