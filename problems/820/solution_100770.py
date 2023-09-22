def posLetra(string,l,n):
    '''...'''
    
    indice=1
    ocorrencias=[]
    
    while len(string)>indice:
        if str.find(string,l)==-1:
            return -1
        elif string[indice]==l:
            ocorrencias=ocorrencias+[indice]
        indice=indice+1
    if len(ocorrencias)<n:
        return -1
    else:
        return ocorrencias[n-1]