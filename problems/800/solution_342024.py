def total (lista, produtos):
    """Função que recebe uma lista de compras em um dicionario que possui o preço dos produtos disponiveis em uma determinada loja,
a função deve retornar o valor total dos itens da lista que estão dispoviveis na loja. list, dic->int"""
    
    soma = 0.00
    i = 0 
    while i<len(lista):
        a=produtos[lista[i]]
        soma=soma+a
        i=i+1
    soma = round (soma,2)
    return soma