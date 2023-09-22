def hashtag(s):
    '''Função que recebe uma string como entrada e retorna a mesma com o caractere # no início, meio e fim dela; string -> string'''
    hashtag = (s%2)
    if len(hashtag)==0:
        return '#'+str(hashtag[:4])+'#'+str(s[4:])+'#'