def divisivel(x):
    r = 0
    for i in range(x):
        if x%(i+1) == 0:
            r = r + 1
    if r>2:
        return false
    elif r<i:
        return true