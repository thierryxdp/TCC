def posLetra(string,letra,indice):
    """Dada uma string uma letra contida na string e um indice de ocorrência
    retorna a posição da ocorrência da letra está na string."""
    while letra in string:
        if letra in string:
            posicao = str.find(string,letra,indice,-1)
            return posicao
        if letra not in string:
            return -1
    return -1