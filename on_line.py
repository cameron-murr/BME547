def point_on_line(tuple1, tuple2, x):
    slope = (tuple2[1] - tuple1[1]) / (tuple2[0] - tuple1[0])
    y = slope * (x - tuple1[0]) + tuple1[1]
    return y

def is_point_in_line(tuple1, tuple2, tuple3):
    slope = (tuple2[1] - tuple1[1]) / (tuple2[0] - tuple1[0])
    y = slope * (tuple3[0] - tuple1[0]) + tuple1[1]

    if tuple3[1] == y:
        return True

    else:
        return False