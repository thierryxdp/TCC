def hashtag(s):
    '''Funcao que recebe uma string e insere um # no inicio, meio e fim da mesma
    str -> str'''

    tamanho = len(s)

    if tamanho%2 == 0:
        intervalo = tamanho//2
    else:
        intervalo = (tamanho-1)//2

    return '#'+s[:intervalo]+'#'+s[intervalo:]+'#'