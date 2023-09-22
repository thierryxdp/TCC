def posLetra(palavra,letra,numero):
    """Retorna a posição na string em que a ocorrência da letra está"""
    a = str.count(palavra,letra)
    if a < numero:
        return -1
    i = 0
    b = str.count(palavra,letra,0,i)
    while b < numero:
        i = i+1
    return i-1