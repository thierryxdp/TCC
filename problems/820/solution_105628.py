def posLetra(string,letra,n):
    ''' funcao que dada uma frase, uma letra e um numero (n) retorna a posicao da enesima ocorrencia da letra na frase. str,str,int -> int'''
    indice = 0
    ocorrencia = 0
    while indice < len(string):
        if letra == string[indice]:
            ocorrencia += 1
        if ocorrencia == n:
            return indice
        if ocorrencia != n:
            indice += 1
    if ocorrencia != n:
        return -1