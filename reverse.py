

#difference between python2 and python3

#python2- strings are stored as ASC11
#python3 - strings are stored as UNICODE
#python2 - 5/2 = 2
#pyhton3 - 5/2 = 2.5
# print function is changed from ' ' to print()
#xrange function resconstructs the sequence every time, and it is replaced by range() in python3
#pyimage libraries are not included in pyhton3
#listcomprehnsion loop  variables bufg has been fixed

#reversal of a string

#enter first name
fname = input("Input your First Name : ")
#enter last name
lname = input("Input your Last Name : ")


rvname = fname[::-1]
rvlast = lname[::-1]

#printing the reverse of a string
print(rvname, rvlast)