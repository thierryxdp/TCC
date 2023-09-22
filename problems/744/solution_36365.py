def hashtag(s):
    """Adiciona "#" no início, no meio e no fim de uma string.
    Assinatura: str -> str
    Casos de teste: 
    hashtag ("tutorial") == '#tuto#rial#'
    hashtag ("cachorro") == '#cach#orro#'
    """
    return '#' + s[0:int(len(s)/2):] + '#' + s[int(len(s)/2):] + '#'