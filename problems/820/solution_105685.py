def posLetra(frase,caracter,n):
    '''Retorna o indice da ocorrencia n do caracter na frase.
    str,str,int -> int'''
    i = 0

    
    while n > 0:
        if not caracter in frase:
            i = -1
            break
        indice = str.index(frase, caracter) + 1
        frase = frase[indice:len(frase)+1]
        n = n -1
        i = i + indice

    return i - 1