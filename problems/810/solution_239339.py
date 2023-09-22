def inverte(f):
    """Dada uma frase de entrada, retorna seu inverso sem a pontuação; str->str"""
    retira_pontuacao=(f=str.replace(f,':',' ')
    f=str.replace(f,';',' ')
    f=str.replace(f,'.',' ')
    f=str.replace(f,'?',' ')
    f=str.replace(f,',',' ')
    f=str.replace(f,'-',' ')
    f=str.replace(f,'!',' ')=f)
    
    listap=str.split(retira_pontuacao(f),' ')
    strinverte=str.join(' ',listap[::-1])
    return strinverte