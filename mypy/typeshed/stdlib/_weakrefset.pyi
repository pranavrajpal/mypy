import sys
from _typeshed import Self
from collections.abc import Iterable, Iterator, MutableSet
from typing import Any, Generic, TypeVar

if sys.version_info >= (3, 9):
    from types import GenericAlias

__all__ = ["WeakSet"]

_S = TypeVar("_S")
_T = TypeVar("_T")

class WeakSet(MutableSet[_T], Generic[_T]):
    def __init__(self, data: Iterable[_T] | None = ...) -> None: ...
    def add(self, item: _T) -> None: ...
    def clear(self) -> None: ...
    def discard(self, item: _T) -> None: ...
    def copy(self: Self) -> Self: ...
    def pop(self) -> _T: ...
    def remove(self, item: _T) -> None: ...
    def update(self, other: Iterable[_T]) -> None: ...
    def __contains__(self, item: object) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __ior__(self: Self, other: Iterable[_T]) -> Self: ...  # type: ignore[override,misc]
    def difference(self: Self, other: Iterable[_T]) -> Self: ...
    def __sub__(self: Self, other: Iterable[Any]) -> Self: ...
    def difference_update(self, other: Iterable[Any]) -> None: ...
    def __isub__(self: Self, other: Iterable[Any]) -> Self: ...
    def intersection(self: Self, other: Iterable[_T]) -> Self: ...
    def __and__(self: Self, other: Iterable[Any]) -> Self: ...
    def intersection_update(self, other: Iterable[Any]) -> None: ...
    def __iand__(self: Self, other: Iterable[Any]) -> Self: ...
    def issubset(self, other: Iterable[_T]) -> bool: ...
    def __le__(self, other: Iterable[_T]) -> bool: ...
    def __lt__(self, other: Iterable[_T]) -> bool: ...
    def issuperset(self, other: Iterable[_T]) -> bool: ...
    def __ge__(self, other: Iterable[_T]) -> bool: ...
    def __gt__(self, other: Iterable[_T]) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def symmetric_difference(self, other: Iterable[_S]) -> WeakSet[_S | _T]: ...
    def __xor__(self, other: Iterable[_S]) -> WeakSet[_S | _T]: ...
    def symmetric_difference_update(self, other: Iterable[_T]) -> None: ...
    def __ixor__(self: Self, other: Iterable[_T]) -> Self: ...  # type: ignore[override,misc]
    def union(self, other: Iterable[_S]) -> WeakSet[_S | _T]: ...
    def __or__(self, other: Iterable[_S]) -> WeakSet[_S | _T]: ...
    def isdisjoint(self, other: Iterable[_T]) -> bool: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...
