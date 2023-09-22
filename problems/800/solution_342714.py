def total(lista_compra,preços):
    '''Função que retorna o valor total do intes da lista de compra
que estejam disponíveis na loja;
    list,dict -> int'''
    t=0
    for elemento in range(len(lista_compra)):
        t=t+preços[lista_compra[elemento]]
    return t