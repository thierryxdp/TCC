def hashtag(s):
    """Insere # no inicio, meio e final da string 
    recebe str e retorna tupla"""
    s="#"+s[:(s)//2]+"#"+s[len(s)//2:]+"#"
    return s