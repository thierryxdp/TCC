def posLetra (frase,letra,n):
    '''Função que retorna qual a localização de uma letra dentro de uma frase dada na entrada da função.
    str, str, int -> int'''
    i = 0
    p = str.find(frase,letra)
    while i < 0 -1:
        if letra in frase:
            p = str.find(frase, letra, p+1)
        i = i + 1
    return p