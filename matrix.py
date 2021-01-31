import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        
        if self.h == 1:
            deter = self.g[0][0]
        
        elif self.h == 2:
            deter = float((self.g[0][0]*self.g[1][1]) - float(self.g[1][0]*self.g[0][1]))
        
        return deter

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        
        sum_diag = 0
        for i in range(self.h):
            sum_diag += self.g[i][i]
        
        return sum_diag

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        
        inver_matrix = []
        inver_determinant = float(1/Matrix.determinant(self))

        if self.h == 1:
            inver_matrix.append([inver_determinant])
        
        elif self.h == 2:
            inver_matrix.append([float(inver_determinant*self.g[1][1]),float( -inver_determinant*self.g[0][1])])
            inver_matrix.append([float(-inver_determinant*self.g[1][0]),float(inver_determinant*self.g[0][0])])
        
        return Matrix(inver_matrix)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        T_matrix = []
        
        for i in range(self.h):
            temp_row = []
            for j in range(self.w):
                temp_row.append(self.g[j][i])
            T_matrix.append(temp_row)
        
        return Matrix(T_matrix)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 

        new_matrix = []
        for i in range(self.h):
            temp = []
            for j in range(self.h):
                temp.append(self.g[i][j] + other.g[i][j])
            new_matrix.append(temp)
        return Matrix(new_matrix)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """

        new_matrix = []
        for i in range(self.h):
            temp = []
            for j in range(self.h):
                temp.append(-self.g[i][j])
            new_matrix.append(temp)
        
        return Matrix(new_matrix)
                

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
    
        
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same")
        
        new_matrix = []
        for i in range(self.h):
            temp = []
            for j in range(self.h):
                temp.append(self.g[i][j] - other.g[i][j])
            new_matrix.append(temp)
            
        return Matrix(new_matrix)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """

        if self.w != other.h:
            raise(ValueError, "Matrices can not be multiplied, incompatible dimensions") 

        new_matrix = []
        for i in range(self.h):
            temp = []
            for j in range(other.w):
                sum_row = 0
                for k in range(self.w):
                    sum_row += (self.g[i][k]*other.g[k][j])
                temp.append(sum_row)
            new_matrix.append(temp)
        
        return Matrix(new_matrix)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        new_matrix = []
        if isinstance(other, numbers.Number):
            for i in range(self.h):
                new_row = []
                for j in range(self.w):
                    new_row.append(self.g[i][j]*other)
                new_matrix.append(new_row)
                
        return Matrix(new_matrix)
            
        
