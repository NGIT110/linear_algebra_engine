### README INFO ###
Used 3 different errors rather than a single MatrixError to improve its usability by external users.

I introduced a subtract dunder method, however, I could have used scalar multiplication by negative 1 and then added to avoid repeating similar code, however by using a sub dunder it makes it easier for a user to complete a subtraction rather than having to wait for 2 operations.
In making __truediv__, I repeted similar code to __mul__ to avoid double rounding to improve accuracy.

### New Learnings ###

# Strassen's Algorithm
This Matrix Multiplication algorithm has time complexity O(n^2.81) and is in theory marginally faster than using IJK loops. However, since Strassen's Algorithm (a divide-and-conquer method) involves recursively splitting 2 matrices into 4 sub matrices, computing 7 intermediate matrix products and performing many matrix additions and subtractions, it introduces immense memory churn and high constant-factor overhead which especially breaks the time constraint in python compared to low-level languages like C as each addition or subtraction carries massive interpreter overhead.

Therefore, this algorithm is only more efficient when matices become incredibly large and in python this cannot be reached due to limited RAM. This means IKJ loops are actually faster to complete.

# Laplace Expansion
A method used to calculate the **determinant** of a large square matrix (3 × 3 or larger) by breaking it down into a sum of smaller, manageable determinants (called submatrices or minors).

1. **Pick a Target:** Choose **any single row** or **any single column** in the matrix. 
   * *Pro-Tip:* Always choose the row or column with the **most zeros**, because multiplying by zero cancels out that entire step and saves you doing math!

2. **The Sign Checkerboard:** Every position in a matrix has a hidden sign (+ or -) based on a grid pattern. It always starts with a `+` in the top-left corner and alternates:
   ```text
   [ +  -  + ]
   [ -  +  - ]
   [ +  -  + ]
   ```
   Keep track of the signs for the row or column you chose.

3. **Cross Out and Multiply:** Walk through your chosen row or column item by item:
   * **Take the number** at that position.
   * **Apply its sign** from the checkerboard grid.
   * **Cross out** its entire row and column. 
   * **Find the determinant** of the leftover mini-matrix (for a $3 \times 3$, this leaves a $2 \times 2$ grid).
   * **Multiply** that mini-determinant by your signed number.

4. **Sum It Up:** Add all of your results from Step 3 together. The final total is your final determinant!

# Gaussian Elimation with Partial Pivoting
**Gaussian elimination with partial pivoting** is an algorithm used to solve linear equations ($Ax = b$) by transforming a matrix into an upper triangular form while rearranging rows to protect against rounding errors.

---

* **The Problem:** Standard elimination breaks down if a diagonal element (the **pivot**) is $0$ (causing division by zero) or extremely small (magnifying tiny numerical round-off errors into massive failures).
* **The Fix:** Before eliminating a column, the computer looks at the current pivot and all numbers directly below it. It finds the entry with the **largest absolute value** and swaps its entire row to the top.

---

1. **Scan:** Look down the active column from the current diagonal position.
2. **Find:** Locate the largest absolute value in that column segment.
3. **Swap:** Swap the current row with the row containing that maximum value.
4. **Eliminate:** Clear out all numbers below the new, stable pivot using standard row reduction.

---

| Pivoting Type | Search Area | Complexity | Use Case |
| :--- | :--- | :--- | :--- |
| **Partial** | Down the current column only | $O(n^2)$ | **Standard.** Ideal balance of speed and numerical accuracy. |
| **Complete** | Entire remaining submatrix | $O(n^3)$ | **Rare.** Too computationally slow for minimal extra accuracy. |

# Matrix Inversion (`notes.md`)

## 1. Core Concept
The **inverse** of a square matrix A (written as A⁻¹) is the matrix that cancels A out when multiplied together, leaving the **Identity Matrix (I)**:

\[A \times A^{-1} = A^{-1} \times A = I\]

* **Identity Matrix (I):** The matrix equivalent of the number 1. It has 1s on the main diagonal and 0s everywhere else. Multiplying any matrix by I leaves it unchanged.

### When Does an Inverse Exist?
A matrix can **only** be inverted if it meets two conditions:
1. **It must be square:** Same number of rows and columns (n × n).
2. **It must be non-singular:** Its determinant cannot be zero (\(\det(A) \neq 0\)). If \(\det(A) = 0\), the matrix "squishes" data flat and cannot be reversed.

---

## 2. How Gauss-Jordan Elimination Works
To find A⁻¹ in code for any n × n matrix, we use **Gauss-Jordan Elimination**:

1. **Augment:** Glue the identity matrix I onto the right side of A to create a wide n × 2n grid: \([A \mid I]\).
2. **Row Reduce:** Use legal row operations to turn the left side (A) into the identity matrix (I).
3. **Extract:** Every operation done to the left side is also applied to the right side. Once the left side becomes I, the right side has transformed into A⁻¹: \([I \mid A^{-1}]\).

### The 3 Legal Row Operations
* **Swap:** Switch the positions of two rows.
* **Scale:** Multiply or divide an entire row by a non-zero number.
* **Eliminate (Combine):** Add or subtract a multiple of one row from another row.

### Why Partial Pivoting?
Computers store decimals with tiny rounding errors. Before cleaning up column i, we look down that column and **swap the row with the largest absolute value** into the diagonal pivot spot. This prevents division by zero and keeps floating-point math accurate.



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

# Matrix Determinants
Laplace Expansion has a tiem complexity of O(n!), which is much less time efficient than Gaussian Elimination with larger matrices as it has a time complexity of O(n^3). Therefore, using Gaussian elimantion with partial pivoting was the more efficient method.