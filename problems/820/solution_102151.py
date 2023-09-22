def posLetra(frase,l,n):
    '''Função que retorna a posição na string está acorrencia 
    da letra dada na entrada
    str,str, int -> int'''
    i = 0 
    p = []
    while len(frase)>i:
        if str.find(frase,l) == -1:
            return -1
        elif frase[i] == l:
            p = p + [i]
        i = i + 1
    if len(p)<n:
        return -1
    else:
        return p[n-1]