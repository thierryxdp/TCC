def total (compras,mercado):
    '''
    Função que recebe uma lista de compras e um dicionario 
    contendo o preço de cada produto disponivel em uma loja,
    e retorna o valor total de itens da lista que estejam 
    disponiveis nesta loja
    lista, dicionario ---> float
    '''
    soma=0
    for n in compras:
        if n in mercado:
            soma+=mercado[n]
    return round(soma,2)