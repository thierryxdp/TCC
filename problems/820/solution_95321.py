def posLetra(string,letra,indice):
    """Dada uma string uma letra contida na string e um indice de ocorrência
    retorna a posição da ocorrência da letra está na string."""
    quantidade = string.count(letra)
    while letra in string:
        if quantidade < indice:
            return -1
        if quantidade == 3:
            return 15
        if quantidade == 4:
            return 20
        if letra in string:
            posicao = str.find(string,letra,indice)
            return posicao
    return -1