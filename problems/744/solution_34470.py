def hashtag(s):
    '''Insere uma # no início, meio e fim de uma string de entrada
    str -> str'''
    x = len(s)//2
    y = "#"+[:x]+"#"+[x:]+"#"
    return y