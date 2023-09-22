def hashtag(s):
    '''Função que recebe uma string como entrada e retorna a mesma com o caractere # no início, meio e fim dela; string -> string'''
    if len(s):
        return'#'+str(s[:4])+'#'+str(s[4:])+'#'
    else:
        if len(s):
            return'#'+str(s[:0])+'#'+str(s[0:]+'#'