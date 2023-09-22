def posLetra(string, letra, numero):
    '''função que verifica e retorna qual posição na string de entrada uma letra desejada está, quando não ocorrida no número desejado, retorna -1; str, str, int -> int'''
    
    if numero > string.count(letra):
        return -1
    
    i = 0
    a = []
    while i < len(string):
        if string[i] == letra:
          a.append(i)
        i = i+1
    return a[numero-1]