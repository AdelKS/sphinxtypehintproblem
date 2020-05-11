import cython

__all__ = ['TestClass']

cdef class TestClass:

    @cython.embedsignature
    def __init__(self, a: str, b: int):
        """
            Docstring text for init
        """