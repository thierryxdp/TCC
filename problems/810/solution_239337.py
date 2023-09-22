def retira_pontuacao(f):
    f=str.replace(f,':',' ')
    f=str.replace(f,';',' ')
    f=str.replace(f,'.',' ')
    f=str.replace(f,'?',' ')
    f=str.replace(f,',',' ')
    f=str.replace(f,'-',' ')
    f=str.replace(f,'!',' ')
    return f

def inverte(f):
    """Dada uma frase de entrada, retorna seu inverso; str->str"""
    listap=str.split(retira_pontuacao(f),' ')
    strinverte=str.join(' ',listap[::-1])
    return strinverte