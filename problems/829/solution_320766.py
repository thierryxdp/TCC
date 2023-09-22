def soma_h(n):
    sum = 1
    for i in range(n):
        if (i == 0):
            continue
            sum = sum+(1/i)
    return round(sum,2)