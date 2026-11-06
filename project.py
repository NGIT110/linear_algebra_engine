class DimensionMismatchError(Exception):
    '''Raised when matrices are incompatible'''
    pass

class SingularMatrixError(Exception):
    '''Raised when matrix has determinant 0'''
    pass

class InvalidMatrixError(Exception):
    '''Raised when matrix is not valid'''
    pass


class Matrix:
    '''Defines a matrix'''

    def __init__(self, data):

        if len(data) == 0: # Checks if matrix is empty
            raise InvalidMatrixError("Matrix cannot be empty")

        if len(data[0]) == 0: # Check if first row is empty
            raise InvalidMatrixError("Rows cannot be empty")

        if not all(len(row) == len(data[0]) for row in data): # Checks if all rows are same length
            mismatched_indices = [i for i, sub in enumerate(data) if len(sub) != len(data[0])] #  Finds all rows where lengths do not match
            raise InvalidMatrixError(f"Matrix is missing an element at row(s): {mismatched_indices}")

        try:
            self.data = [[float(val) for val in row] for row in data] # Unpacks the 2D array 

        except (ValueError, TypeError):
            raise InvalidMatrixError("Elements in a matrix must be numbers")

        self.rows = len(self.data)
        self.cols = len(data[0])


        






