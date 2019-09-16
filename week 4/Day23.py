
#day 23

#Exercise 1
myinfo={
"Name":"ashwag" ,
"Age":30 ,
"City":"Riyadh"
}

if "Name" in myinfo:
    print ("Name in the my info")


#Exercise 2
myinfo={
"Name":"ashwag" ,
"Age":30 ,
"City":"Riyadh"
}
print (len(myinfo))


#Exercise 3
myinfo={
"Name":"ashwag" ,
"Age":30 ,
"City":"Riyadh"
}
myinfo["country"]="saudi arabia"
print (myinfo)



#Exercise 4
myinfo={
"Name":"ashwag" ,
"Age":30 ,
"City":"Riyadh"
}
myinfo.pop("Name")
print (myinfo)


#Exercise 5
myinfo={
"Name":"ashwag" ,
"Age":30 ,
"City":"Riyadh"
}
myinfo.popitem()
print (myinfo)



#Exercise 6
myinfo={
"Name":"ashwag" ,
"Age":30 ,
"City":"Riyadh"
}
myinfo.clear()
print (myinfo)
