def sqrt(n):
    if n < 0:
        raise ValueError("{} is a negative number "
                         "which is not allowed".format(n))

    if n is type(str):
        raise TypeError("Cannot send a string")

    x = n
    y = 1

    # e decides the accuracy level

    e = 0.000001

    while(x - y > e):
        x = (x + y) / 2
        y = n / x

    return x
