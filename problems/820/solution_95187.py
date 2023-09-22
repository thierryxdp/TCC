def posLetra (string,letra,n):
    '''Retorna a posição da ocorrência n da letra na string fornecida.
    str, str, int ->: int'''
    contador = 0
    lista = []
    posicao = 0
    if n>str.count(string, letra):
        return -1
    while contador < len (string):
        if string[posicao] == letra:
            list.append (lista,posicao)
        contador = contador +1 
        posicao = posicao + 1
    return lista[n-1]