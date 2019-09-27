

#day 34

#Exercise 1
def myfun(numb):
    for x in numb:
        print(x)


number =[1,2,3,4,5,6]

myfun(number)

#Exercise 2
def myfun2(x):
    return 3 * x

print (myfun2(4))
print (myfun2(7))


#Exercise 3
def myfun3(City ,name ):
    print('My City is '+ City)


myfun3( name ='ashwag',City='Jeddah')


#Exercise 4
def myfun4(*info ):
    print('My City is '+ info[1])


myfun4( 'ashwag','Jeddah' )


#Exercise 5

def myfunrec(n):
    if (n>0):
        result = n + myfunrec(n-1)
        print(result)
    else:
        result =0
    return result


myfunrec(7)
