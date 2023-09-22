def posLetra(string,letra,numero):
    '''retorna a posicao em que a ocorrencia da letra dada como entrada está
    tupla -> int'''
    a=0
    b=0
    if numero > str.count(string,letra):
        return -1
    while a < len(string) and b < numero:
        v=string[a]
        if v == letra:
            b=b+1
        a=a+1
    if b == numero:
        return a-1