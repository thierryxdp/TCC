def retira_pontuacao(f):
    """dada uma frase retira todos os caracteres de pontuacao e troca por espacos str->str"""
    if '-' in f:
        f=str.replace(f,'-',' ')
    if ',' in f:
        f=str.replace(f,',','')
    if ':' in f:
        f=str.replace(f,':',' ')
    if ';' in f:
        f=str.replace(f,';','')
    if '.' in f:
        f=str.replace(f,'.','')
    if '?' in f:
        f=str.replace(f,'?','')
    if '!' in f:
        f=str.replace(f,'!','')
    return f