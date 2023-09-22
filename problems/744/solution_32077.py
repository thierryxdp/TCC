'''Esta função recebe como parâmetro uma string e retorna uma string com
o # no início, meio e fim da mesma.
str --> str'''
def hashtag(s):
    meio = len(s)//2
    var = '#'+s[:meio]+'#'+s[meio:]+'#'
    return var