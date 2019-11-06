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


if __name__ == "__main__":
    test5 = q5_string()
    test5.getString()
    test5.printString()