def posLetra(palavras,letra,numero):
    """Retorna a posição na string em que a ocorrência da letra está. str, str,int -> int"""
    a = str.count(palavras,letra)
    if a < numero:
        return -1
    i = 0
    b = str.count(palavras,letra,0,i)
    while b < numero:
        i = i+1
        b = str.count(palavras,letra,0,i)
    return i-1