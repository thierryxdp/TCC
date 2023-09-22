def posLetra(string,l,n):
    '''
    A função retorna a posição da letra
    de acordo com numero que indica a
    ocorrencia dela.
    string,string,int -> int
    '''
    i = 0
    nr = 0
    
    while i < len(string):
        if string[i] == l:
            nr = nr + 1
            if n == nr:
                return i
        i = i + 1
        
    return -1