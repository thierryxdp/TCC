def retira_pontuacao(f):
    if '-' in f:
        f=str.replace(f,'-',' ')
    if ',' in f:
        f=str.replace(f,',',' ')
    if ':' in f:
        f=str.replace(f,':',' ')
    if ';' in f:
        f=str.replace(f,';',' ')
    if '.' in f:
        f=str.replace(f,'.',' ')
    if '?' in f:
        f=str.replace(f,'?'.' ')
    if '!' in f:
        f=str.replace(f,'!'.' ')
    return f