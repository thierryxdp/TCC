def hashtag(s):
    '''Função que receba uma string e insera o caractere # no início, no meio e no final dela; string -> string'''
    if len(s%2)==3:
        return '#'+str(s[:1.5])+'#'+str(s[1.5:])+'#'
    else:
        return '#'+str(s[0:4])+'#'+str(s[4:])+'#'