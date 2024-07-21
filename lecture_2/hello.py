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

# define a set
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
s.remove(2)
print(s)
print(f"The set has {len(s)} elements.")

# define a tuple
coordinate = (10.0, 20.0)

n = int(input("Number:"))

if(n > 0):
    print("n is positive")
elif(n < 0):
    print("n is negative")
else:
    print("n is zero")

# for loop

for i in [0, 1, 2, 3, 4]:
    print(i)

for i in range(6):
    print(i)


# for-each loop
flowers = ["rose", "lily", "tulip"]
for flower in flowers:
    print(flower)