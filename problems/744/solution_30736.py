def hashtag(s):
    """a função hashtag ao receber uma string irá inserir "#" no início,
    no meio e no final da string
    str -> str"""
    
    return str("#") + str(s)[0:len(s)//2] + str("#") + str(s)[len(s)//2:] + str("#")