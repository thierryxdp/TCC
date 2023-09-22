def posLetra(string, letra, numero):
    '''função que verifica e retorna qual posição na string de entrada uma letra desejada está, quando não ocorrida no número desejado, retorna -1; str, str, int -> int'''
    
    if numero > string.count(letra):
        return -1
    
    i = 0
    while i < len(string):
        return string.index(letra, numero)