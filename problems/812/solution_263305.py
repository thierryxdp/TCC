def retira_pontuacao(f):
    if '-' in f:
        str.replace(f,'-',' ')    
    if ',' in f:
        str.replace(f,',',' ')
    if ':' in f:
        str.replace(f,':',' ')
    if ';' in f:
        str.replace(f,';',' ')
    if '.' in f:
        str.replace(f,'.',' ')
    return f