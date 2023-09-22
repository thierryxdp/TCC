def hashtag (n):
    '''função que recebe uma string(n) e insere o caractere (#) no início, meio e fim dela; string -> strig'''
    return '#'+n[0:(len(n)//2)]+'#'+n[(len(n)//2):]+'#'