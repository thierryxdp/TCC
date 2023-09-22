def total(x,y):
    soma=0
    for mercadoria in range(len(x)):
        if x[mercadoria] in y:
            soma = soma + y[x[mercadoria]]
    return soma