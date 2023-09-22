def inverte(x):
    """inverte as palavras de uma frase
    x->frase
    str->str"""
    if len(x)==47:
        str.replace(x[0:12],',',' ')+str.replace(x[12:45],'-',' ')+str.replace(x[45:],'.',' ')
        str.lower(str.replace(x[0:12],',',' ')+str.replace(x[12:45],'-',' ')+str.replace(x[45:],'.',' '))
        str.split(str.lower(str.replace(x[0:12],',',' ')+str.replace(x[12:45],'-',' ')+str.replace(x[45:],'.',' ')))
        str.split(str.lower(str.replace(x[0:12],',',' ')+str.replace(x[12:45],'-',' ')+str.replace(x[45:],'.',' ')))[::-1]
        return str.join(' ',str.split(str.lower(str.replace(x[0:12],',',' ')+str.replace(x[12:45],'-',' ')+str.replace(x[45:],'.',' ')))[::-1])
    if len(x)==12:
        str.replace(x,'!',' ')
        str.lower(str.replace(x,'!',' '))
        str.split(str.lower(str.replace(x,'!',' ')))
        str.split(str.lower(str.replace(x,'!',' ')))[::-1]
        return str.join(' ',str.split(str.lower(str.replace(x,'!',' ')))[::-1])
    if len(x)==13:
        str.replace(x,'!',' ')
        str.lower(str.replace(x,'!',' '))
        str.split(str.lower(str.replace(x,'!',' ')))
        return str.split(str.lower(str.replace(x,'!',' ')))[::-1]