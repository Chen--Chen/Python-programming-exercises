import math
import numpy as np
################# question 1 ###################
def q1_div(x,y):
    l=[]
    for i in range(x,y):
        if (i%7==0) and (i%5!=0):
            l.append(str(i))
    l_cont = ','.join(l)
    print(type(l_cont),(l_cont))

################# question 2 ###################
def q2_factorial(x):
    for i in range(x-1,1,-1):
        x=x*i
    print(x)
def q2_factorial_s(x):
    if x==0:
        return 1
    else:
        return x*q2_factorial_s(x-1)

################# question 3 ###################
def q3_sqr(x):
    d = {}
    for i in range(1,x+1):
        d[i]=i*i
    return(d)

################# question 4 ###################
def q4_listtuple_s():
    values=input()
    l=values.split(",")
    t=tuple(l)
    print(l)
    print(t)

################# question 5 ###################
class q5_string:
    def __init__(self):
        self.get_string=""
    def getString(self):
        self.get_string=input()
    def printString(self):
        print(self.get_string.upper())

#test5 = q5_string()
#test5.getString()
#test5.printString()

################# question 6 ###################
def q6_sqr_func(c=50,h=30):
    value =[]
    items=[x for x in input().split(',')]
    for d in items:
        value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
    print(','.join(value))

################# question 7 ###################
# defined using numpy, return numpy.ndarray
def q7_array_build(x,y):
    a = np.zeros(shape=(x,y))
    for i in range(0,x):
        for j in range(0,y):
            a[i][j] = i*j
    print(a)
    return(a)

# defined using list of list, return list
def q7_array_build_s():
    input_str = input()
    dimensions=[int(x) for x in input_str.split(',')]
    rowNum=dimensions[0]
    colNum=dimensions[1]
    multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

    for row in range(rowNum):
        for col in range(colNum):
            multilist[row][col]= row*col
    print(multilist)
    return(multilist)


 ################# question 8 ###################   
def q8_sort_words():
    x_string = input()
    x_list = [x for x in x_string.split(',')]
    x_list.sort()
    print(','.join(x_list))
 
 ################# question 9 ################### 
def q9_capitilize_string():
    x_string = input()
    print(x_string.upper())



if __name__ == "__main__":
    q9_capitilize_string()