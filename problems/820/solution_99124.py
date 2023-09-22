def posLetra(s,l,n):
    '''Recebe uma frase 's' e retorna a posição em que o caractere 'l' completa sua 'n'ésima ocorência. Caso seja impossível obedecer essas condições, retorna -1, string->int '''
    proximo=0
    ocorrencias=0
    while proximo<len(s) and ocorrencias<n:
        if s[proximo]==l:
            ocorrencias=ocorrencias+1
            proximo=proximo+1
        else:
            proximo=proximo+1
    return proximo