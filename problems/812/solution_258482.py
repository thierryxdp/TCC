def retira_pontuacao(f):
    """Dada um frase f, retorna a mesma sem pontuação; str->str"""
    f=str.replace(f,':',' ')
    f=str.replace(f,';',' ')
    f=str.replace(f,'.',' ')
    f=str.replace(f,'?',' ')
    f=str.replace(f,',',' ')
    f=str.replace(f,'-',' ')
    f=f.strip()
    return f