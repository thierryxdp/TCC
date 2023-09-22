def inverte(f):
    """Dada uma frase de entrada, retorna seu inverso sem a pontuação; str->str"""
def rp(f):
    f=str.replace(f,':',' ')
    f=str.replace(f,';',' ')
    f=str.replace(f,'.',' ')
    f=str.replace(f,'?',' ')
    f=str.replace(f,',',' ')
    f=str.replace(f,'-',' ')
    f=str.replace(f,'!',' ')
    return f
    listap=str.split(rp(f),' ')
    strinverte=str.join(' ',listap[::-1])
    return strinverte