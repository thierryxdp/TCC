def inverte(frase):
    """calculo e retorno de uma funcao que retorne outra frase numa ordem inversa"""
    a=str.replace(frase,'.',' ')
    b=str.replace(a,',',' ')
    c=str.replace(b,'-',' ')
    d=str.replace(c,'!',' ')
    e=str.replace(d,'?',' ')
    return e