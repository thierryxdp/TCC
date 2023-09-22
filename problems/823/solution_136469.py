def faltante(lista):
    """Dado uma lista de números, retorna o número faltante entre 1 e o número mais alto da lista,
    limitado a apenas um número faltante; list -> int"""
    lista.sort()
    tamanho = len(lista)
    x = 1
    if lista[0] == 2:
        return 1
    elif tamanho == 1:
        return 2
    while x < tamanho:
        posicao1 = lista[x]-1
        posicao2 = lista[x-1]
        if posicao1 != posicao2:
            return posicao1
        x=x+1
        if x == lista[tamanho-1]:
            return lista[tamanho-1]+1