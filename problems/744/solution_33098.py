# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
# função que recebe uma string e insere um '#' no início, no meio e no final dela
def hashtag(s):
    'str -> str'
    if len(s)%2==0:
        pausa=len(s)//2
    else:
        pausa=(len(s)-1)//2
    return '#'+s[:pausa]+'#'+s[pausa:]+'#'