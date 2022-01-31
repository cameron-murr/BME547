def point_on_line(tuple1, tuple2, x):
    slope = (tuple2[1] - tuple1[1]) / (tuple2[0] - tuple1[0])
    y = slope * (x - tuple1[0]) + tuple1[1]
    return y
