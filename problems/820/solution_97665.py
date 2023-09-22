def posLetra(texto,letra,n=1):
    '''Retorna a posicao da letra na n-esima ocorrencia
    dela dentro do texto(se nao houver a n-esima ocorrencia
    da letra no texto retorna -1).
    str,str,int -> int'''
    ocorrencia = str.find(texto,letra)
    k = 1
    while k < n:
        ocorrencia = str.find(texto,letra,(ocorrencia+1))
        k += 1
    return ocorrencia