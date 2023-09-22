def total (lista, produtos):
    """A função recebe uma lista de compras em um dicionario contendo o preço dos produtos disponiveis em uma determinada loja,
a função deve retornar o valor total dos itens da lista que estão dispoviveis na loja. list, dic->int"""
    
    soma = 0.00
    i = 0 
    while i<len(lista):
        a=produtos[lista[i]]
        soma=soma+a
        i=+1
    soma = round (soma,2)
    return soma