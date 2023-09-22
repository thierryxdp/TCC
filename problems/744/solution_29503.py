def hashtag(s):
    """recebe uma string e insere o # no inicio, meio e final
    str->str"""
    
    meio = len(s)//2
    
    return '#'+s[0:meio]+'#'+s[meio:]+'#'