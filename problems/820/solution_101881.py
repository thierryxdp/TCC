def posLetra(string,letra,n):
    
    '''
    funcao que recebe uma string, uma letra e um n
    e retorna a posicao da ocorrencia n da letra.
    str,str, int - int
    '''
    pos = []
    i = 0
    while i < len(string):
        if string[i] == letra:
            pos.append(i)
    
        i = i+1
    return pos[n-1]