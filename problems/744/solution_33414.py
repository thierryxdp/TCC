def hashtag(s):
    '''Função que recebe uma string como entrada e retorna a mesma com o caractere # no início, meio e fim dela; string -> string'''
    if len(s):
        return'#'+str(s[:4])+'#'+str(s[4:])+'#' and '#'+str(s[:2])+'#'+str(s[2:])+'#'