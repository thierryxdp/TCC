def media_matriz(x):
    a=[]
    for i in range(len(x)):
        a.append(sum(x[i]))
    return round(sum(a)/(len(a)*len(x[0])),2)