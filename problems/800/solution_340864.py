def total(lista,produtos):
    soma_produtos = 0
    for i in range(len(lista)):
        soma_produtos = soma_produtos + produtos[lista[i]]
    return round(soma_produtos,2)