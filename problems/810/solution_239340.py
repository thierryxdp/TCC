def inverte(f):
    """Dada uma frase de entrada, retorna seu inverso sem a pontuação; str->str"""
    rp=(f=str.replace(f,':',' ')
        f=str.replace(f,';',' ')
        f=str.replace(f,'.',' ')
        f=str.replace(f,'?',' ')
        f=str.replace(f,',',' ')
        f=str.replace(f,'-',' ')
        f=str.replace(f,'!',' '))
    listap=str.split(rp,' ')
    strinverte=str.join(' ',listap[::-1])
    return strinverte