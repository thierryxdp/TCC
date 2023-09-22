def total(lista,produtos):
    soma_produtos = 0
    for i in range(len(dict.keys(produtos))):
        soma_produtos = soma_produtos + produtos[lista[i]]
    return soma_produtos