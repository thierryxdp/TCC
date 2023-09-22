# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' Retorna a string s com o caracter especial # no inicio meio e fim, separando 
        em duas partes a string para posicionar o # no centro dele'''
    d = len(s)/2
    return '#'+s[:int(d)] + '#' + s[int(d):] + '#'