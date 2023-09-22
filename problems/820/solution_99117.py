def posLetra(s,l,n):
    ''' '''
    proximo=0
    ocorrencias=0
    while proximo<len(frase) and ocorrencias<n:
        if frase[proximo]==l:
            ocorrencias=ocorrencias+1
    proximo=proximo+1
    return proximo