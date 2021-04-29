from node import Node


class Container(Node):
    __slots__ = ()


class Hashable(Node):
    __slots__ = ()


class Iterable(Node):
    __slots__ = ()


class Sized(Node):
    __slots__ = ()


class Callable(Node):
    __slots__ = ()


class Iterator(Iterable):
    __slots__ = ()


class Reversible(Iterable):
    __slots__ = ()


class Generator(Iterator):
    __slots__ = ()


class Collection(Sized, Iterable, Container):
    __slots__ = ()


class Sequence(Reversible, Collection):
    __slots__ = ()


class MutableSequence(Sequence):
    __slots__ = ()


class ByteString(Sequence):
    __slots__ = ()


class Set(Collection):
    __slots__ = ()


class MutableSet(Set):
    __slots__ = ()


class Mapping(Collection):
    __slots__ = ()


class MutableMapping(Mapping):
    __slots__ = ()


class MappingView(Sized):
    __slots__ = ()


class ItemsView(MappingView, Set):
    __slots__ = ()


class KeysView(MappingView, Set):
    __slots__ = ()


class ValuesView(MappingView, Collection):
    __slots__ = ()
