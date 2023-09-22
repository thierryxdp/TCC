def posLetra(frase,letra,ocorrencia):
    ''' 
    Recebe um texto, uma letra l e n é o numero de ocorrência a ser pesquisada
    Retorna um int com o numero de ocorrencias
    '''
    i = 0
    N_ocorrencia= 0
    while i<len(frase) and N_ocorrencia<ocorrencia:
        if frase[i] == letra:
            N_ocorrencia +=1
        i = i + 1
    if N_ocorrencia < ocorrencia:
        return -1
    else:
        return i-1