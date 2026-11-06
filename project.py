class DimensionMismatchError(Exception):
    '''Raised when matrices are incompatible'''
    pass

class SingularMatrixError(Exception):
    '''Raised when matrix has determinant 0'''
    pass

class InvalidMatrixError(Exception):
    '''Raised when matrix is not valid'''
    pass