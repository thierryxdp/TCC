def inverte(x):
    """inverte as palavras de uma frase
    x->frase
    str->str"""
    if len(x)==47:
        return str.replace(x[0:12],',',' ')+str.replace(x[12:45],'-',' ')+str.replace(x[45:],'.',' ')
        return str.lower(str.replace(x[0:12],',',' ')+str.replace(x[12:45],'-',' ')+str.replace(x[45:],'.',' '))