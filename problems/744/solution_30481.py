def hashtag(s: str)-> str:
    '''retorna uma nova string com # no início, no meio e no fim da string dada'''
    return "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"