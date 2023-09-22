# str-> str
def hashtag(s):
    '''uma string que insere o caractere "#" no início, meio e fim da própria string.
    str -> str'''
    meio = len(s)/2
    return '#'+s[0:meio]+'#'+s[meio:]