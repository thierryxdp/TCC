def repetidos(x):
    
    repetidos= []
    i = 0
    while x[i] <= x[-1]:
        if x[i] == x[i+1]:
            list.append(repetidos, x[i])
            i = i +1
        elif x[i] != x[i+1]:
            i=i+1
        
    return len(repetidos)