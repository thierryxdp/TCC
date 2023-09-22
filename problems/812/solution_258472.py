def  removePontuacao(f):
    f=str.replace(f,':',' ')
    f=str.replace(f,';',' ')
    f=str.replace(f,'.',' ')
    f=str.replace(f,'?',' ')
    f=str.replace(f,',',' ')
    f=str.replace(f,'-',' ')
    f=str.replace(f,'!',' ')
    f=str.replace(f,'  ',' ')
    f=f.strip()
    return f