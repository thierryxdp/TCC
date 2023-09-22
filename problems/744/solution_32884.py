# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    'Entrada = string ; saída = string'
    par = len(s)%2
    metade = len(s)//2
    impar = len(s) - 1
    metade2 = impar//2
    if par == 0:
        return '#'+s[:metade]+'#'+s[metade:]+'#'
    elif par!=0:
        return '#'+s[:metade2]+'#'+s[metade2:]+'#'