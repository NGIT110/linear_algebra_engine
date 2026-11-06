class DimensionMismatchError(Exception):
    '''Raised when matrices are incompatible'''
    pass

class SingularMatrixError(Exception):
    '''Raised when matrix has determinant 0'''
    pass

class InvalidMatrixError(Exception):
    '''Raised when matrix is not valid'''
    pass


class Matrix():
    '''Defines a matrix'''

    def __init__(self, data):

        if len(data) == 0: # Checks if matrix is empty
            raise InvalidMatrixError("Matrix cannot be empty")

        expected = len(data[0])

        if expected == 0: # Check if first row is empty
            raise InvalidMatrixError("Rows cannot be empty")

        if not all(len(row) == expected for row in data): # Checks if all rows are same length
            mismatched_indices = [i for i, sub in enumerate(data) if len(sub) != expected] #  Finds all rows where lengths do not match
            raise InvalidMatrixError(f"Matrix is missing an element at row(s): {mismatched_indices}")

        try:
            self.data = [[float(val) for val in row] for row in data] # Converts each element to float then then builds new list

        except (ValueError, TypeError):
            raise InvalidMatrixError("Elements in a matrix must be numbers")

        self.rows = len(self.data)
        self.cols = expected

    def __str__(self):

        max_width = max(len(f"{element:.4f}") for row in self.data for element in row) # Finds widest formatted string 

        string_rows = []
        for row in self.data:
            aligned_elements = [f"{element:.4f}".rjust(max_width) for element in row] # Right aligns every element with the mximum width
            string_rows.append(" ".join(aligned_elements)) # Joins elements with spaces

        return "\n".join(string_rows) # Joins rows with newlines

    def __add__(self, other):
        '''Adds 2 matrices'''

        if not isinstance(other, Matrix): # Checks if other is also matrix
            return NotImplemented # Signals operator doesn't support addition of non-matrices
        
        if self.rows != other.rows or self.cols != other.cols:
            raise DimensionMismatchError(f"Cannot add {self.rows}x{self.cols} matrix to {other.rows}x{other.cols} matrix")

        new_matrix = Matrix([[a+b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(self.data, other.data)])

        return new_matrix

        
# Iterative tests
A = Matrix([[1, 2], [2, 3]])
B = Matrix([[2, 0], [4, 1]])
 
print(A+B)
    

        






