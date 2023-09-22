def total(lista_de_compras,produtos):
    soma=0
    for mercadoria in range(len(lista_de_compras)):
        if lista_de_compras[mercadoria] in produtos:
            soma = soma + produtos[lista_de_compras[mercadoria]]
    return round(soma,2)