def melhor_volta(a):
    t1 = 0
    t2 = 10000
    t3 = 0
    for x in range(len(a)):
        for y in range(len(a[x])):
            if a[x] < t2:
                t1 = x
                t2 = a[x]
                t3 = y
    return (t1,t2,t3)