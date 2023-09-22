def hashtag(s):
    '''função que retorna o caractere '#' no inicio,no meio e no final da string: str->str'''
    meio = len(s)//2
    return '#'+s[0:meio]+'#'+s[meio:]+'#'