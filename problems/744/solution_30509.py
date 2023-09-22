def hashtag(s):
    """Funcao que recebe uma string e retorna uma string com '#' no começo, meio e fim: str=>str"""
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s