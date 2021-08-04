import numpy as np
class matrix:
    def __init__(self, values):
     self.values= values
    def helper(x) :
        ans = [[0 for c in range(len(x.values[0]))] for r in range (len(x.values))]
        return ans

    def __add__(self,other) :
     ans = self.helper()

     if (len(self.values) == len(other.values) and len(self.values[0]) == len(other.values[0])) :
        y=0
        for i in self.values :
            if (len(i) != len(other.values[y])) :
                raise ValueError('Dimensions are different')
            z=0    
            for k in i:
                ans[y][z] = (other.values)[y][z] + k
                z+=1
            y+=1
        return matrix(ans)
 
     else:
        raise ValueError("Matrices have different dimensions")

    
    def __sub__(self,other) :
     ans = [[0 for c in range(len(self.values[0]))] for r in range (len(self.values))]

     if (len(self.values) == len(other.values) and len(self.values[0]) == len(other.values[0])) :
        y=0
        for i in self.values :
            if (len(i) != len(other.values[y])) :
                raise ValueError('Dimensions are different')
            z=0    
            for k in i:
                ans[y][z] = k - (other.values)[y][z] 
                z+=1
            y+=1
        return matrix(ans)
 
     else:
        raise ValueError("Matrices have different dimensions")

    
    def __mul__(self,other) :
     ans = [[0 for c in range(len(other.values[0]))] for r in range (len(self.values))]

     if (len(self.values[0]) == len(other.values)):
        for i in range(len(self.values)):

            for j in range(len(other.values[0])):
                for k in range(len(other.values)):
                    ans[i][j] += (self.values)[i][k] * (other.values)[k][j]
        return matrix(ans)
     else:
        raise ValueError("Matrices have dimensions invalid for multiplication")

    def cofactor(m, i, j):
        return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]

    def __det__(self) :
        # if (len(self.values[0]) == len(self.values)):
        #     n_array = np.array(self.values)
        #     det = np.linalg.det(n_array)
        #     return det
        # else:
        #     raise ValueError("Matrices must be square")
     def cofactor(m, i, j):
        return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]

     if(len(self.values[0]) == len(self.values)):
        if(len(self.values) == 2):
            value = self.values[0][0] * self.values[1][1] - self.values[1][0] * self.values[0][1]
            return value
        Sum = 0
        for current_column in range(len(self.values)):
            sign = (-1) ** (current_column)
            cf= cofactor(self.values, 0, current_column)
            sub_det = __det__(cf)
            Sum += (sign * self.values[0][current_column] * sub_det)
    
        return Sum
     else:
        raise ValueError("Matrices must be square")
    


    def __pow__ (self, n) :
        ans = self
        for i in range(n-1) :
            ans = ans * self
        return matrix(ans)

# a= matrix([[1,0],[0,1]])
# b= matrix([[2,0],[0,2]])
# print((a + b).values)
# print((a - b).values)
# print((a * b).values)
# print((b ** 3).values.values)

