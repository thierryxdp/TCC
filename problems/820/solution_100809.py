def posLetra(string,letra,n):
    '''
       função que retorna em que posicao da string a letra
       indicada pela ocorrencia n está
       str, str, int -> int
    '''
    ocorrencias = string.count(letra)
    i = 0
    quantidade = 0
    if ocorrencias<n:
        return -1
    else:
        while quantidade<n:
            if string[i] == letra:
                quantidade = quantidade + 1
            i=i+1
        return i - 1