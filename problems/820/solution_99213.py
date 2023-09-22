def posLetra(string, letra, n):
    ''' Fazer uma funcao que retorne em que posicao da string a ocorrencia da letra esta;
    str, str, int -> int'''
    
    i = 0
    posicao = [ ] 
    
    while i < len(string):
        if string[i] == letra:
            pos = str.find(string, letra, i)
            posicao += [pos,]
        i = i + 1
    if len(posicao) < n:
        return -1
    else:
        return posicao[n - 1]