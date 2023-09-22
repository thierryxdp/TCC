def posLetra(string,letra,n):
    
    '''recebe uma string, uma letra e qual a ocorrência n da letra na string e retorna a posição onde se encontra a ocorrência dada,
    caso a ocorrência não exista na string, retorna -1.
    (str,str,int) -> int'''
    
    posicao = 0
    lista = []
    
    if n > str.count(string, letra):
        return -1
    
    while posicao < len(string):
        if string[posicao] == letra:
            list.append (lista,posicao)
        posicao = posicao + 1
    return lista[n]