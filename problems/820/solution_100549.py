def posLetra(texto,l,n):
    '''
    recebe como entrada uma string, uma letra l e um número
    n que indica a ocorrencia desejada de l, retorna a 
    posição da string em que a ocorrencia n da letra esta
    str, str, int->int
    '''
    i=0
    j=0
    if str.count(texto,l)<n:
        return -1
    
    while j<n:
        if texto[i]==l:
            j=j+1
        i=i+1
    return i-1