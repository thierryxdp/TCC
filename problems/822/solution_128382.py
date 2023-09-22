def posLetra(string,letra,n):
    ''' retona em qual posição da string a ocorrencia da letra está'''
    p = 0
    i = 0
    while i < len(string):
        if string[i]==letra:
            p = p+1
            if p < n:
                p = -1