def hashtag(s):
    '''Insere uma # no início, meio e fim de uma string de entrada
    str -> str'''
    x = len(s)//2
    return "#"+[0:x]+"#"[x:]+"#"