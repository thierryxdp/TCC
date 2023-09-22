def total(x,y):
    soma=()
    for mercadoria in range(len(x)):
        if x[mercadoria] in y:
            soma = soma + y[x[mercadoria]]
    return soma