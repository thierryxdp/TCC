def posLetra(string,l,n):
    '''Recebe uma string, uma letra e um numero que indica a ocorrencia e retorna
    em que posição da string aqauela ocorrencia da letra se encontra.
    str,str,int->int'''
    
    indice=0
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