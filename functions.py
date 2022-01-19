def add(a, b):
    if (a or b) < 0:
        return "No negatives"
    c = a + b
    d = a - b
    return c,d

x,y = add(1,2)
print(x)
print(y)
#print(x[0])
#print(x[1])