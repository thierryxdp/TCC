def repetidos(l):
    count = 0
    for i in range(len(l)):
        if l[i] == l[i-1]:
            count += 1
    return count