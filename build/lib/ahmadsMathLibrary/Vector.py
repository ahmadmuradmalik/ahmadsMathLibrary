
class Vector:
    def __init__(self, vector_data):
        self.data = [float(xi) for xi in vector_data]
        self.size = len(vector_data)
        if self.size == 0:
            return ValueError("Sorry cannot gimme an empty vector right now")
    
    def add(self, v):
        if not isinstance(v, Vector):
            v = Vector(v)
        if v.size != self.size:
            return ValueError("Sorry vectors must be of the same size")
        for i, val in enumerate(v.data):
            self.data[i] += val
        return self.data
        
    def subtract(self, v):
        if not isinstance(v, Vector):
            v = Vector(v)
        if v.size != self.size:
            return ValueError("Sorry vectors must be of the same size")
        for i, val in enumerate(v.data):
            self.data[i] -= val
        return self.data

    def self_outer(self):
        from ahmadsMathLibrary.linear_algebra import mat_mat
        #returns outer product of our vector with it self. assuming our
        #vectors are of size (n x 1) , then the outerproduct will be (n x n)
        #self.data = [1, 2, 3, 4, 5]
        #transpose = [[1], [2], [3], [4], [5]]
        transpose = [[vi] for vi in self.data]
        #now self.data = (5 x 1)
        #transpose = (1 x 5)
        #in theory mat_mat(self.data, transpose) should return
        #the outer product (5 x 5) matrix
        return mat_mat(transpose, [self.data])
    
    def outer(self, v):
        pass
    
    def self_inner(self):
        from ahmadsMathLibrary.linear_algebra import dot
        return dot(self.data, self.data)
    
    def dot(self, v):
        from ahmadsMathLibrary.linear_algebra import dot
        return dot(self.data, v)
    
        
            
        