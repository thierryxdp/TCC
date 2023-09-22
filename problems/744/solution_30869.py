def hashtag(str):
    """Recebe uma string e insere o caracte # no início, meio e fim
    dela.
    Entrada: string
    Saída: string
    """
    y=len(str)
    x=len(str)/2-1
    return '#' + '[:x] + '#' + [x:] + '#'