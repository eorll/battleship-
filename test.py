l = [2,5,4,3,6,7,8,5,4]
b = [-8, 42, 18, 0, -16]

print(len(b)-1)
# [-16, -8, 0, 18, 42]


def mirror(mylist):
    sort = sorted(mylist)
    rsort = sorted(mylist, reverse=True)
    return sort + rsort[1:]


print(mirror(b))

print("\u001b[31mWorld\u001b[37m")
print("Wojtek")

