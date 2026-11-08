import math

# Global constants
EPSILON = 1e-9

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
            raise DimensionMismatchError(f"Cannot add a {self.rows}x{self.cols} from a {other.rows}x{other.cols} matrix")

        new_matrix = Matrix([[a+b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(self.data, other.data)])

        return new_matrix

    def __sub__(self, other):
        '''Subtracts 1 matrix from another'''

        if not isinstance(other, Matrix):
            return NotImplemented 
        
        if self.rows != other.rows or self.cols != other.cols:
            raise DimensionMismatchError(f"Cannot subtract a {other.rows}x{other.cols} from a {self.rows}x{self.cols} matrix")

        new_matrix = Matrix([[a-b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(self.data, other.data)])

        return new_matrix

    def __mul__(self, other):
        '''Multiplies matrix by scalar'''

        if isinstance(other, float) or isinstance(other, int):
            return Matrix([[a*other for a in row_a] for row_a in self.data])
        else:
            return NotImplemented

    def __rmul__(self, other):
        '''Completes reverse multiplication if self is the scalar'''
        return self * other

    def __neg__(self):
        '''Returns negative matrix'''
        return self * -1

    def __truediv__(self, other):
        '''Completes true division'''

        if not isinstance(other, float) and not isinstance(other, int):
            return NotImplemented

        if other == 0:
            raise ZeroDivisionError("division by 0")

        return Matrix([[a / other for a in row_a] for row_a in self.data])

    def __matmul__(self, other):
        '''Multiplies 2 matrices'''

        if not isinstance(other, Matrix):
            return NotImplemented 

        if self.cols != other.rows:
            raise DimensionMismatchError(f"Cannot multiply a {self.rows}x{self.cols} matrix with a {other.rows}x{other.cols} matrix")

        result_data = [[0.0 for _ in range(other.cols)] for _ in range(self.rows)] # Initialises resulting matrix with correct size

        # Completes matrix multiplication with 3 loops - O(n^3)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result_data[i][j] += self.data[i][k] * other.data[k][j]

        return Matrix(result_data)

    @classmethod
    def identity(cls, n):
        '''Creates an identity Matrix'''

        identity_data = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    identity_data[i][j] = 1

        return cls(identity_data)

    def is_square(self):
        '''Checks if a matrix is a square'''
        return self.rows == self.cols

    def __eq__(self, other):
        '''Checks for equality'''
    
        if not isinstance(other, Matrix):
            return NotImplemented 

        if self.rows != other.rows or self.cols != other.cols: # Checks if 2 matrices are same shape
            return False

        # Compares each corresponding element
        for row_a, row_b in zip(self.data, other.data):

            if not all(math.isclose(a, b, abs_tol=EPSILON) for a, b in zip(row_a, row_b)): # Checks for approximate eqaulity
                return False

        return True

    def __repr__(self):
        '''Represents Matrix in string form for testing'''
        return f"Matrix({self.data})"


def determinant(matrix):
    '''Returns Determinant of a matrix'''

    if not isinstance(matrix, Matrix):
        raise InvalidMatrixError("Not a valid matrix, so cannot find determinant")

    if not matrix.is_square():
        raise DimensionMismatchError("Cannot find determinant of non-square matrix")

    matrix_copy = matrix


def _gaussian_elimination(data):
    '''Helper for determinant function'''





if __name__ == "main":
    # Iterative tests
    A = Matrix([[1, 2], [2, 3]])
    B = Matrix([[2, 0], [4, 1]])
 
    print(B - A)
    print(A.is_square())


        






