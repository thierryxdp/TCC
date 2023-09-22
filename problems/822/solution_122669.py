def repetidos(x):
    y = []
    repetidos= []
    i = 0
    while x[i] != x[-1]:
        if x[i] == x[i+1]:
            list.append(repetidos, x[i])
            i = i +1
        elif x[i] != x[i+1]:
            i=i+1
     y = len(repetidos)
    
    if x[i] == x[-1]:
        return y+1
    elif x[i] != x[-1]:
        return y