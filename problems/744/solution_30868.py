def hashtag(s):
    """Recebe uma string e insere o caracte # no início, meio e fim
    dela.
    Entrada: string
    Saída: string
    """
    x=len(s)/2-1
    return '#' + s[:x] + '#' + [x:] + '#'