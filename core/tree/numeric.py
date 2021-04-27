from methods import Add, Sub, Mul, TrueDiv, Pow, Neg, Pos, Abs, \
    FloorDiv, Mod, DivMod, LShift, RShift, And, Xor, Or, Invert
from node import FuncLike


class Complex(FuncLike):  # C
    __slots__ = ()
    methods = {Add, Sub, Mul, TrueDiv, Pow, Neg, Pos, Abs}


class Float(Complex):  # R
    __slots__ = ()
    methods = {*Complex.methods, FloorDiv, Mod, DivMod}


class Exact(Float):  # Q
    __slots__ = ()


class Integer(Float):  # Z
    __slots__ = ()
    methods = {*Exact.methods, LShift, RShift, And, Xor, Or, Invert}


class Natural(Integer):  # N
    __slots__ = ()
