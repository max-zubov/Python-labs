from random import randint

class Matrix:
    
    def __init__(self, data_list, m=0, n=0):
        
        if not isinstance(data_list, list): 
            raise ValueError('Not list in arguments')
        if not(isinstance(m, int) and isinstance(n, int)): 
            raise ValueError('M*N not integer in arguments')
        
        if (m*n>0):
            # Init matrix from list
            if (m*n==len(data_list)):
                self.__matr = [[data_list[i*n+j] for j in range(n)] for i in range(m)]
            # Init random (m*n) matrix
            elif len(data_list)==0:
                self.__matr=[[randint(0, 9) for _ in range(n)] for _ in range(m)]
            else: 
                raise ValueError('Matrix size not equal list size')
        # Init of matrix by 2d array
        else: 
            m=len(data_list)    
            try:                
                n=len(data_list[0])  
            except:         #except if data_list not array
                raise ValueError('Data not array.')
            try:
                for i in range(m):
                    if n!=len(data_list[i]):
                        raise ValueError('Data not array.')
            except:         #except if data_list not array
                raise ValueError('Data not array.')
            self.__matr = data_list
        self.__row=m
        self.__col=n
        
        
    @property
    def row(self):    return self.__row

    @property
    def col(self):    return self.__col

    @property
    def matr(self):    return self.__matr

    
    def is_identity(self):
        if self.row!=self.col: return False
        for i in range(self.row):
            for j in range(self.col):
                if(self.matr[i][j]!=1 if i==j else self.matr[i][j]!=0): return False
                #if ((i==j) and (self.matr[i][j]!=1)) or ((i!=j) and (self.matr[i][j]!=0)) : return False
        return True

        
    def is_square(self):
        return self.row==self.col
        
    def is_zero(self):
        for i in range(self.row):
            for j in self.matr[i]:
                if j!=0: return False
        return True    
        
    def is_diagonal(self):
        if self.row!=self.col: return False
        for i in range(self.row):
            for j in range(self.col):
                if (i!=j) and (self.matr[i][j]!=0) : return False         
        return True
         
    def transpose(self):
        self.__matr = [[self.matr[j][i] for j in range(self.row)] for i in range(self.col)] 
        #self.__matr = [list(item) for item in zip(*self.matr)]
        self.__row, self.__col = self.__col, self.__row
    
    def draw(self):
        for i in range(self.row) : 
            for j in range(self.col) : 
                print("{:3}".format(self.matr[i][j]),end=" ")
            print()     
        print()
        
    def __str__(self):
        return "{}".format(self.matr)
        

    def __add__(self, a):
        if (self.row!=a.row or self.col!=a.col):
            raise ValueError('Matrix sizes are different.')
        rezult = [[self.matr[i][j]+a.matr[i][j] for j in range(self.col)] for i in range(self.row)]
        return Matrix(rezult)
            
    def __sub__(self, a):
        if (self.row!=a.row or self.col!=a.col):
            raise ValueError('Matrix sizes are different.')
        rezult = [[self.matr[i][j]-a.matr[i][j] for j in range(self.col)] for i in range(self.row)]
        return Matrix(rezult)
        
    def __mul__(self, a):
        if (self.col!=a.row):
            raise ValueError('Number of columns in first matrix is not equal to number of columns in second matrix.')
        result=[]
        for i in range(self.row):
            for j in range(a.col):
                s=0
                for k in range(self.col):
                    s += self.matr[i][k]*a.matr[k][j] 
                result.append(s)
        return Matrix(result,self.row,a.col)
        

class HorizontalVector(Matrix):
    def __init__(self, data_list,ln=0):
        if ((len(data_list)==0) and (ln==0)):
            raise ValueError('Error init vector data.')
        if ln==0: ln=len(data_list)
        super(HorizontalVector, self).__init__(data_list,1, ln)


class VerticalVector(Matrix):
    def __init__(self, data_list,ln=0):
        if ((len(data_list)==0) and (ln==0)):
            raise ValueError('Error init vector data.')
        if ln==0: ln=len(data_list)
        super(VerticalVector, self).__init__(data_list, ln, 1)
