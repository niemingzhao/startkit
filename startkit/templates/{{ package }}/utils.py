# -*- coding: utf-8 -*-


def with_metaclass(*classes):
    def func(x): return '_'.join(i.__name__ for i in x)
    metaclass = tuple(set(type(cls) for cls in classes))
    metaclass = type(func(metaclass), metaclass, {})
    return metaclass(func(classes), classes, {})
