def posLetra(s,l,i):
    ''' recebe uma string, uma letra e um numero inteiro da ocorrencia
    dessa letra e retorna a posiçao em que a letra se encontra
    entrada: str, int
    saida: int'''
    p = s.find(l)
    while p >= 0 and i > 1:
        p = s.find(l,p+1)
        i = i-1
    return p