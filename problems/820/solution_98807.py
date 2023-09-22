def posLetra(palavra,letra,numero):
    """Retorna a posição na string em que a ocorrência da letra está"""
    a = str.count(palavra,letra)
    if a < numero:
        return -1