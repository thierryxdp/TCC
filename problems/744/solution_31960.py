def hashtag(s):
    '''Função que adiciona # ao início, meio e fim de uma string; string->string'''
return '#'+str(s)[:len(s)//2]+'#'+[len(s)//2+1:]+'#'