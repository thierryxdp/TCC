def hashtag(s):
    """retorna uma string igual a primeira com a adiçao de caracteres '#' no inico, meio e fim
    str--->str"""
    metade_s= len(s)//2
    return '#'+s[0:metade_s]+'#'+s[metade_s:]+'#'