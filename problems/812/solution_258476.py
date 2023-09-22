def  retira_pontuacao(f):
    f=str.replace(f,':',' ')
    f=str.replace(f,';',' ')
    f=str.replace(f,'.',' ')
    f=str.replace(f,'?',' ')
    f=str.replace(f,',',' ')
    f=str.replace(f,'-',' ')
    f=str.replace(f,'!',' ')
    f=str.replace(f,' ',' ')
    f=f.strip()
    return f