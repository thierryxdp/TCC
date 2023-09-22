def posLetra(s,l,n):
    ''' '''
    proximo=0
    ocorrencias=0
    while proximo<len(s) and ocorrencias<n:
        if s[proximo]==l:
            ocorrencias=ocorrencias+1
    proximo=proximo+1
    return proximo