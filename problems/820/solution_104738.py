def posLetra(texto, l, n):
    '''
    Recebe um texto, uma letra l e n é o numero de ocorrência a ser pesquisada
    Retorna um int com o numero de ocorrencias 
    '''
    correncias = []
    for c in enumerate(texto):     
        if c[1] == l:               
            correncias.append(c[0])  
    if n >= len(correncias):
        return -1 
    return correncias[n - 1]