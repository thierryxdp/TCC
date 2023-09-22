def total(lista,preco):
    """."""
    soma = 0
    tamanho_da_lista = len(lista)
    for i in range(0, tamanho_da_lista):
        produto = lista[i]
    if produto in preco :
        custa =  dict.get(preco,lista[1])
        soma += custa
    return round(soma,2)