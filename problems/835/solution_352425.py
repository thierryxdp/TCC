def melhor_volta(mat):
    a = [item for sublist in mat for item in sublist]
    b = min(a)
    c = a.index(b)
    d = c+1
    if c in range(10):
        return (1,b,d)
    elif c in range(11,20):
        return (2,b,d-10)
    elif c in range(21,30):
        return (3,b,d-20)
    elif c in range(31,40):
        return (4,b,d-30)
    elif c in range(41,50):
        return (5,b,d-40)
    elif c in range(51,60):
        return (6,b,d-50)