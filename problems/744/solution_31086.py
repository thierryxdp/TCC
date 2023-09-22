def hashtag(texto):
    '''retorna a string dada com o caracter "#" inserido no inicio, meio e final dela; str->str'''
    x=texto
    y=len(x)
    z=int((y//2))
    return '#'+x[0:z]+'#'+x[z:]+'#'