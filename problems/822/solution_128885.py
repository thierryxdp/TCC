def repetidos(ls):
    x=0
    y=ls[1:len(ls)]
    for m in range(len(y)):
        if ls[m]==y[m]:
            x=x+1
    return x