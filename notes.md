### README INFO ###
Used 3 different errors rather than a single MatrixError to improve its usability by external users.

I introduced a subtract dunder method, however, I could have used scalar multiplication by negative 1 and then added to avoid repeating similar code, however by using a sub dunder it makes it easier for a user to complete a subtraction rather than having to wait for 2 operations.
In making __truediv__, I repeted similar code to __mul__ to avoid double rounding to improve accuracy.

### New Learnings ###

# Strassen's Algorithm
This Matrix Multiplication algorithm has time complexity O(n^2.81) and is in theory marginally faster than using IJK loops. However, since Strassen's Algorithm (a divide-and-conquer method) involves recursively splitting 2 matrices into 4 sub matrices, computing 7 intermediate matrix products and performing many matrix additions and subtractions, it introduces immense memory churn and high constant-factor overhead which especially breaks the time constraint in python compared to low-level languages like C as each addition or subtraction carries massive interpreter overhead.

Therefore, this algorithm is only more efficient when matices become incredibly large and in python this cannot be reached due to limited RAM. This means IKJ loops are actually faster to complete.

### Algorithmic optimisation ###

# Matrix Multiplication
This is a O(n^3) complex procedure without using any external functions:
Initially, I used 3 loops:
    # Completes matrix multiplication with 3 loops - O(n^3)
    for i in range(self.rows):
        for j in range(other.cols):
            for k in range(self.cols):
                result_data[i][j] += self.data[i][k] * other.data[k][j]

Then I tried to find more efficient ways and came across -transposition-:
    # This allows fast row-by-row streaming instead of column indexing
    transposed_other = list(zip(*other.data))
    return [[sum(a * b for a, b in zip(row_A, col_B)) for col_B in B_T] for row_A in A]
However, this doubles the memory complexity while still remaning as O(n^3). It is only faster due to the heavy optimisation of zip() and sum() under the hood in C which improves the efficiency.

I also came across Strassen's algorithm - mentioned in New Learnings section.