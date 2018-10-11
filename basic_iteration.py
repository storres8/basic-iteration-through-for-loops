# exmaple of iteration through a basic list
my_list=[1,2,3,4,5]
for num in my_list:
    print(num)
# prints out
# 1
# 2
# 3
# 4
# 5

# we can also check and print only even numbers
for num in my_list:
    if num % 2 == 0:
        print(num)
# prints out
# 2
# 4

# iteration through a list of tuples
my_list2=[(11,12), (13,14), (15,16)]

for a,b in my_list2:
    print(a)
    print(b)
# prints:
# 11
# 12
# 13
# 14
# 15
# 16

# iteration through a dictionary
# we can use .items() to grab key and value
# or .keys() for keys
# or .values() for the values


d={"k1":1, "k2":2, "k3":3, "k4":4}
for key,value in d.items():
    print(key)
    print(value)

# prints:
# k1
# 1
# k2
# 2
# k3
# 3
# k4
# 4
