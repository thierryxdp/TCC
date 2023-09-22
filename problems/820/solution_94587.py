def posLetra(texto,letra,n):
    '''Função que retonar em qual posição se encontra uma letra dada a 
    ocorrência; string, string, int -> int'''
    
    if n>texto.count(letra):
        return -1
    i=0
    Oc=[]
    while i<len(texto):
        if texto[i] == letra:
            list.append(Oc,i)
        i = i + 1
    return Oc[n-1]