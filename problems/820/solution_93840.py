def posLetra(frase,letra,numero):
    '''
    A função retorna a posição da letra
    de acordo com numero que indica a
    ocorrencia dela.
    string,string,int -> int
    '''
    indice = 0
    numerorepetido = 0
    
    while indice < len(frase):
        if frase[indice] == letra:
            numerorepetido = numerorepetido +1
            if numero == numerorepetido:
                return indice
        indice = indice+1
        
    return -1