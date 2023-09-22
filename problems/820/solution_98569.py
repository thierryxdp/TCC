def posLetra(frase,letra,n):
    '''Recebe uma frase, letra e numero e retorna o indice da ocorrencia n da letra informada na frase.
    str,str,int -> int'''
    i=0
    while n != 0:
        if frase[i] == letra:
            n = n-1
        i = i+1
    return i-1