def melhor_volta(m):
    x =[]
    for i in range(len(m)):
        x.append(min(m[i]))
    y= min(x)
    return (y.find(x)+1,y,10)