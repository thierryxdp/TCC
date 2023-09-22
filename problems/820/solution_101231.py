def posLetra(frase,letra,ocorrencia):
    '''recebe uma string e retorna a posição da ocorrência'''
    
    i=0
    rep=0
    
    while i<len(frase) and rep<ocorrencia:
        if frase[i] == letra:
            rep = rep + 1
        i=i+1
    if rep<ocorrencia:
        return -1
    else:
        return i-1