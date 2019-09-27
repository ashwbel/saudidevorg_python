

#day 36

#Exercise 1
def myfun1(n):
    return lambda  a:a + n

mynum= myfun1(5)
print(mynum(9))



#Exercise 2
def myfun2(n):
    return lambda  a:a + n

mynum1= myfun2(5)
mynum2= myfun2(6)
print(mynum1(9))
print(mynum2(9))
