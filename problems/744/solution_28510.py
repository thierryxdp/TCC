def hashtag(s):
    """Função que recebe uma string e retorna ela com # no início, meio e final 
    str -> str"""
    meio = len(s)//2
    return '#'+s[0:meio]+'#'+s[meio:len(s)]+'#'