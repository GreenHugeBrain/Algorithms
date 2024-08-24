def simple(start, end):
    arr = []
    for num in range(start, end):
        counter = 0
        for i in range(1, num + 1):
            if num % i == 0:
                counter += 1
        if counter == 2:
            arr.append(num)
    return arr
            

print(simple(1, 33))