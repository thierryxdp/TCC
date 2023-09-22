def hashtag(s):
    """Recebe uma string e retorna uma nova com 'hashtags', #, no início meio
    e fim da mesma.

    Parâmetros: s -> str
    Retorno: str
    """

    i=len(s)//2
    ns='#'+s[0:i]+'#'+s[i:]+'#'
    return ns