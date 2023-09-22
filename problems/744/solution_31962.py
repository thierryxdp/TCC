def hashtag(s):
    '''Função que adiciona # ao início, meio e fim de uma string; string->string'''
    return '#'+str(s)[0:len(s)//2]+'#'+str(s)[(len(s)+1)//2:]+'#'