# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''A partir da string s retorna-a adicionando hashtag no inicio, meio
    e fim dela
    str -> str'''
    n = len(s)
    if n/2 == n//2:
        return '#'+s[:int(n/2)]+'#'+s[int(n/2):]+'#'
    elif n/2 != n//2:
        return '#'+s[:int((n-1)/2)]+'#'+s[int((n-1)/2):]+'#'