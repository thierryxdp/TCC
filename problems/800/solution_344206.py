def total(x,y):

    soma = 0
    
    for i in x:
        if i in y:
         soma += y[i]

    return round(soma,2)