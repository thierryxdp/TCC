def hashtag(s):
    ''' retorna uma string com # no início, no meio e no final;
    str->str '''
    return '#'+s[:len(s)//2]+'#'+s[len(s)//2:]+'#'