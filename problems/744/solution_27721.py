def hashtag(s):
    """função que recebe uma string e insere o caractere "#" no início, meio e final dela"""
    return '#'+s[0:len(s)//2]+'#'+s[len(s)//2:len(s)]+'#'