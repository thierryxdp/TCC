def even(start, n):
    count = []

    for i in range(start, n):
        if 1 <= start and n <= 100:
            if i % 2 == 0:
                count.append(i)
    return [count]