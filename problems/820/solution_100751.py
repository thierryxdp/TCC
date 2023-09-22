def posLetra(string,l,n):
    '''...'''
    
    indice=1
    ocorrencias=[]
    
    while len(string)>indice:
        if str.find(string,l)==-1:
            return -1