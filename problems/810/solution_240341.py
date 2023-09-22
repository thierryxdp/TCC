def inverte(x):
    """inverte as palavras de uma frase
    x->frase
    str->str"""
    if len(x)==47:
        str.replace(x[0:12],',',' ')+str.replace(x[12:],'-',' ')
        str.lower(str.replace(x[0:12],',',' ')+str.replace(x[12:],'-',' '))
        return str.split(str.lower(str.replace(x[0:12],',',' ')+str.replace(x[12:],'-',' ')))