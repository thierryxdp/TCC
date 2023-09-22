def posLetra(string,letra,indice):
    """Dada uma string uma letra contida na string e um indice de ocorrência
    retorna a posição da ocorrência da letra está na string."""
    while letra in string:
        if letra in string:
            posicao = str.find(string,letra,indice)
            return posicao
    return -1