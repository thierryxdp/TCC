def rp(f):
    f=str.replace(f,':',' ')
    f=str.replace(f,';',' ')
    f=str.replace(f,'.',' ')
    f=str.replace(f,'?',' ')
    f=str.replace(f,',',' ')
    f=str.replace(f,'-',' ')
    return f
def inverte(z):
    """Dada uma frase de entrada, retorna seu inverso sem a pontuação; str->str"""
    listap=str.split(rp(z),' ')
    strinverte=str.join(' ',listap[::-1])
    return strinverte