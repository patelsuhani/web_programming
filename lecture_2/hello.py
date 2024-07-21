name = input("Name:")
print(f"Hello, {name}!")
print(name[0])

# define a list of names
names = ["David", "Bob", "Charlie"]
print(names)
print(names[0])
names.append("Alice")
names.sort()
print(names)

coordinate = (10.0, 20.0)

n = int(input("Number:"))

if(n > 0):
    print("n is positive")
elif(n < 0):
    print("n is negative")
else:
    print("n is zero")
