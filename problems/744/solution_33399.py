def hashtag(s):
    '''Função que recebe uma string como entrada e retorna a mesma com o caractere # no início, meio e fim dela; string -> string'''
    if len(s):
        return'#'+str(s[:3])+'#'+str(s[3:])+'#'