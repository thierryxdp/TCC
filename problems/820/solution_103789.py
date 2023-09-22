def posLetra(x,l,n):
    '''
    Função que dada uma string, uma letra e um número, indica a ocorrencia desejada
    da letra.
    str, str, int -> str, str, int
    '''
    if str.count(x,l) < n:
        return -1
    
    indice=()
    i=0
    
    while i < len(x):
        if x[i]==l:
            indice = indice + (i,)
        i = i+1
        
    return indice[n-1]