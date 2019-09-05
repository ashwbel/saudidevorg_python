#Exercise 1
wordtup  =('hello','how','why' ,2,4,1)
if 'hello' in wordtup:
    print('helo every one')


#Exercise 2
num=(3,4,5,6)
num = num +(1,2,3)
print(num)


#Exercise 3
tup =(1,5.23,1.2,3.8,3,4,5,6)
print(len(tup))


#Exercise 4
wordtup  =tuple(('hello','how','why' ,2,4,1))
print(wordtup)

#Exercise 5

word  =['hello','how','why' ,2,4,1]
wordtup3 = tuple(word)
print(wordtup3)

#Exercise 6

word  =['hello','hello','hello','how','why' ,2,4,1]
wordtup3 = tuple(word)
print(wordtup3.index('why'))
print(wordtup3.count('hello'))
