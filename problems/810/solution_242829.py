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

def inverte(frase):
    """
    retorna a frase original invertida e sem pontuação
    str -> str
    """
    Nfrase = list(retira_pontuacao(frase))
    list.reverse(Nfrase)
    return ' '.join(Nfrase)