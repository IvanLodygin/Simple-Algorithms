def area(points):
    value = 0.0
    for i in range(len(points)):
        next_i = (i + 1) % len(points)
        value += points[i][0] * points[next_i][1] - points[i][1] * points[next_i][0]
    return abs(value) / 2

def orientation(first, second, third):
    val = (second[1] - first[1]) * (third[0] - second[0]) - (second[0] - first[0]) * (third[1] - second[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return -1

def graham(data: list) -> list:
    for i in range(1, len(data)):
        if data[0][0] > data[i][0]:
            data[0], data[i] = data[i], data[0]

    for i in range(2, len(data)):
        tmp = i
        while tmp > 1 and orientation(data[0], data[tmp - 1], data[tmp]) == 1:
            data[tmp], data[tmp - 1] = data[tmp - 1], data[tmp]
            tmp -= 1

    points_stack = [data[0], data[1]]
    for i in range(2, len(data)):
        while len(points_stack) > 1 and orientation( points_stack[-2], points_stack[-1], data[i] ) == 1:
            points_stack.pop()
        points_stack.append(data[i])

    return points_stack