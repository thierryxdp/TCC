# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que adiciona uma # no inicio, meio e final de uma string
    str->string'''
    total_letras= len(s)
    if total_letras%2==0:
        metade_palavra=len(s)//2
        return '#'+s[0:metade_palavra]+'#'+s[metade_palavra:total_letras]+'#'
    else:
        metade_palavra=(len(s)-1)//2
        return '#'+s[0:metade_palavra]+'#'+s[metade_palavra:total_letras]+'#'