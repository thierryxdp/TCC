def retira_pontuacao(frase):
    """
    retorna a frase original com espaços no lugar de pontuações
    str -> str
    """
    Nfrase = str.replace(frase, '-', ' ')
    Nfrase = str.replace(Nfrase, ',', ' ')
    Nfrase = str.replace(Nfrase, ';', ' ')
    Nfrase = str.replace(Nfrase, ':', ' ')
    Nfrase = str.replace(Nfrase, '...', ' ')
    Nfrase = str.replace(Nfrase, '.', ' ')
    Nfrase = str.replace(Nfrase, '!', ' ')
    Nfrase = str.replace(Nfrase, '?', ' ')

    return Nfrase