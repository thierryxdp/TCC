def inverte(frase):
    """calculo e retorno de uma funcao que retorna o inverso de um frase"""
    x=frase
    a=str.replace(x,',',' ')
    b=str.replace(a,'.',' ')
    c=str.replace(b,'-',' ')
    d=str.replace(c,'?',' ')
    k=str.replace(d,'!',' ')
    e=str.lower(k)
    f=str.split(e)
    g=f[::-1]
    h=str.join(' ',g)
    return h