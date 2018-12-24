fname   =   "clinton"
sname   =   "ogweno"
lname   =   "opiyo"
full    =   f"{fname} {sname} {lname}"
print(full.title())
print(full.find('ogw'))
print('muga' in full)
print('opiyo' in full)
print('mwananyau' not in full)
x=5
print(bin(x))
x=(10**4)
print(x)

#inputs
name    =   str(input("Name: "))
age     =   int(input("Enter Age: "))

#render inputs
print(name)
print(age)



#conditions.

if age <= 18:
    print(f"Sorry, you're under age... You're {age}!")
else:
    print(f"Welcome, {name}...")
    



