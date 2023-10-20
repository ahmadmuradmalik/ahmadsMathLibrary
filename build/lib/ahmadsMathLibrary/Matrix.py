class Matrix:
    def __init__(self, matrix_data):
        self.data = matrix_data
        self.rows = len(matrix_data)
        self.cols = len(matrix_data[0])
        self.size = self.rows, self.cols
        if self.rows == 0 or self.cols == 0:
            return ValueError("Sorry your matrix must not be empty")
    
    def add(self, matrix2):
        #check to see if there is a dimension mismatch
        if len(matrix2) != self.rows or len(matrix2[0]) != self.cols:
            return ValueError("Sorry your matrices must be of the same size")

        #so now matrices are of the same size 
        for i, row in enumerate(matrix2):
            for j, val in enumerate(row):
                self.data[i][j] += val
        return self
    
    



        

    
