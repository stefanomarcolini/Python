# -*- coding: utf-8 -*-

class Matrix:
    '''
        this class contains methods
        for basic operations with
        vectors and matrices
    '''
    
    def __init__(self):
        pass
    
    def sumVectorScalar(self, V, y, subtract = False):
        ''' 
        REQUIRES: Vector[n], float y, bool subtract (default = False)
        MODIFIES: ---
        EFFECT:   returns the sum of a vector and a scalar
        EXAMPLE:  V[n] = [1, 2, 3]
                  y = 2
                  V[n] + y = [3, 4, 5]
                  V[n] - y = [-1, 0, 1]
        '''
        return [V[i] - y if subtract else V[i] + y for i in range(len(V))]

    def sumVectors(self, A, B, subtract = False):
        '''
        REQUIRES: A[n], B[n], bool subtract (default = False)
	    MODIFIES: ---
    	EFFECT:   returns a new vector that is the sum of two vectors
                  if len(A) != len(B) an Exception is raised
        '''
        if len(A) != len(B):
            raise Exception('Invalid input params: vectors must have same length')
        return [A[i] - B[i] if subtract else A[i] + B[i]for i in range(len(A))]
    
    def sumMatrix(self, A, B, subtract = False):
        '''
        REQUIRES: A[m][n], B[m][n], bool subtract (default = False)
	    MODIFIES: ---
    	EFFECT:   returns a new matrix that is the sum of two matrices
                  an Exception is raised if A and B have different dimensions
        '''
        if len(A) != len(B) and len(A[0]) != len(B[0]):
            raise Exception('Invalid input params: matrices must have same dimensions')
        X = []
        for i in range(len(A)):
            X.append([A[i][j] - B[i][j] if subtract else A[i][j] + B[i][j] for j in range(len(A[0]))])
        return X
        
    def sumVectorEntries(self, V):
        '''
        REQUIRES: V[n]
	    MODIFIES: ---
    	EFFECT:   returns the sum of all items
                  sum = V[0] + V[1] + ... + V[n]
        '''
        return sum(V)
    
    def multiplyScalarVector(self, V, y, divide = False):
        '''
        REQUIRES: V[n], float y, bool divide (default = False)
	    MODIFIES: ---
    	EFFECT:   returns the resulting multiplication / division of a vector with a scalar
        '''
        return [1 / y * V[i] if divide else y * V[i] for i in range(len(V))]
    
    def multiplyScalarMatrix(self, M, y, divide = False):
        '''
        REQUIRES: M[m][n], float y, bool divide
	    MODIFIES: ---
    	EFFECT:   returns a new matrix that is the result
                  of the multiplication of a matrix with a scalar
        '''
        X = []
        for i in range(len(M)):
            X.append([1 / y * M[i][j] if divide else y * M[i][j] for j in range(len(M[0]))])
        return X
        
    def multiplyVectors(self, A, B, A_vertical = False):
        '''
        REQUIRES: A[n], B[n], bool A_vertical (default = False)
	    MODIFIES: ---
    	EFFECT:   returns the result of the multiplication
                  of a vector with another vector, checking if the first is a
                  vertical vector (by default False)
                  an Exception is raised if A and B have different dimensions
        '''
        if len(A) != len(B):
            raise Exception('Invalid input params: vectors must have same length')
        if A_vertical:
            X = []
            for i in range(len(A)):
                Y = []
                Y = [A[i] * B[j] for j in range(len(B))]
                X.append(Y)
            return X
        return sum(A[i] * B[i] for i in range(len(A)))

    def multipyVectorMartix(self, M, V, divide = False):
        '''
        IMPORTANT: matrix rows must be equal to vector length
	               in case of division vector must NOT contain 0 (zeros) 
	    REQUIRES:  M[m][n], V[n], bool divide (default = False)
	    MODIFIES:  ---
    	EFFECT:    returns a new vector that is the result of the
                   multiplication of a vector with a matrix
        '''
        if len(M) != len(V):
            raise Exception('Invalid input params: matrix columns length and vector length must match')
        X = []
        for j in range(len(M[0])):
            if divide:
                try:
                    X.append(sum([M[i][j] * 1 / V[i] for i in range(len(M))]))
                except ZeroDivisionError:
                    print('Invalid input: ZeroDivisionError, zero found in vector')
                    return None
            else:
                X.append(sum([M[i][j] * V[i] for i in range(len(M))]))
        return X

    def extractVector(self, M, column):
        '''
            REQUIRES: M[m][n], column (from which to extract the vertical vector)
    	    MODIFIES: ---
            EFFECT:   returns a new vector V[m] that contains all
                      items selected from the specified column of
                      the given matrix
        '''
        try:
            V = [M[i][column] for i in range(len(M))]
        except IndexError:
           raise Exception("Invalid input: column value too large") 
        return V
    
    def multiplyMatrices(self, A, B, divide = False):
        '''
           IMPORTANT: M1 -> matrix[m][N], M2 -> matrix[N][o]
                      in case of divisions, matrix B must NOT contain 0 (zeros)
                      
                      es. M1 = |1  2|  M2 = |3  4  5  6  9|
                               |3  4|       |7  8  9  1  3|
                               |6  5|
                           
           MATRICES MULTIPLICATION IS NON COMMUTATIVE: (A * B) != (B * A)
           MATRICES MULTIPLICATION IS ASSOCIATIVE:     (A * B) * C == A * (B * C)
           
           REQUIRES:  A[m][N], B[N][o], bool divide
           MODIFIES:  ---
           EFFECT:    returns a new matrix that is the result of the
                      multiplication of two matrices
        '''
        if len(A[0]) != len(B):
            raise Exception("Invalid input params: matrix A columns and matrix B rows must have the same length");
        m = Matrix()
        X = []
        for i in range(len(A)):
            X.append(m.multipyVectorMartix(B, A[i], divide))
        return X    
    
    def vectorToMatrix(self, V):
        '''
            REQUIRES:  V[n]
            MODIFIES:  ---
            EFFECT:    returns a new matrix M[n][2] such that 
                       every M[n][0] == 1 && M[n][1] = V[n]
    
            EXAMPLE:   V = [2  3  4] -> M = |1  2|
                                            |1  3|
                                            |1  4|
        '''
        return [[1, V[i]] for i in range(len(V))]
    

    def addOnesToMatrix(self, M):
        '''
        
            REQUIRES:  M[m][n]
            MODIFIES:  ---
            EFFECT:    returns a new matrix M[m][n + 1] 
                       such that every M[m][0] == 1

            EXAMPLE:   M = |2  3  4| -> M1 = |1  2  3  4|
                           |5  6  7|         |1  5  6  7|
        '''
        return [[1] + M[i] for i in range(len(M))]
    
    def identityMatrix(self, dimensions):
        '''
            FOR ANY MATRIX: (X[m][n] * I[n][n]) == (I[m][m] * X[m][n]) == X[m][n]

            REQUIRES:  integer dimension d
            MODIFIES:  ---
            EFFECT:    returns the identity matrix[d][d]

            EXAMPLE: dimensions = 3

                     Identity Matrix:    |1 0 0|
                                         |0 1 0|
                                         |0 0 1|
        '''
        return [[0 if i != j else 1 for i in range(dimensions)] for j in range(dimensions)]
    
    def transpose(self, M):
        '''
            REQUIRES:  M[m][n]
            MODIFIES:  ---
            EFFECT:    returns a new transposed matrix
        '''
        return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]
    
    
    def minor(self, M, row, column):
        '''
        REQUIRES:  M[m][m]  (must be a square matrix)
                   row      index of the row to exclude
                   column   index of the column to exclude
        MODIFIES:  ---
        EFFECT:    returns the minor of the given matrix where all the values
                   of the original matrix are represented, except for those
                   values contained in the selected row and column
        '''
        if row >= len(M):
            raise Exception('Invalid input: row must be less than matrix rows length')
        elif column >= len(M[0]):
            raise Exception('Invalid input: colums must be less than matrix columns length')
        return [[M[i][j] for j in range(len(M)) if j != column] for i in range(len(M)) if i != row]
