
#day 22

#Exercise 1
myinfo={
"Name":"ashwag" ,
"Age":30 ,
"City":"Riyadh"
}
print(myinfo)


#Exercise 2
myinfo={
"Name":"ashwag" ,
"Age":30 ,
"City":"Riyadh"
}
x=myinfo["Name"]
print(x)


#Exercise 3
myinfo={
"Name":"ashwag" ,
"Age":30 ,
"City":"Riyadh"
}
x=myinfo.get("Name")
print(x)


#Exercise 4
myinfo={
"Name":"ashwag" ,
"Age":30 ,
"City":"Riyadh"
}
myinfo["City"] ="Jeddah"
print(myinfo)

#Exercise 5
myinfo={
"Name":"ashwag" ,
"Age":30 ,
"City":"Riyadh"
}

for x in myinfo :
    print (x)


#Exercise 6
myinfo={
"Name":"ashwag" ,
"Age":30 ,
"City":"Riyadh"
}

for x in myinfo :
    print (myinfo[x])


#Exercise 7
myinfo={
"Name":"ashwag" ,
"Age":30 ,
"City":"Riyadh"
}

for x in myinfo.values() :
    print (x)


#Exercise 8
myinfo={
"Name":"ashwag" ,
"Age":30 ,
"City":"Riyadh"
}

for x ,y in myinfo.items() :
    print (x ,y)
