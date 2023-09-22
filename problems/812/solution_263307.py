def retira_pontuacao(f):
    nova=''
    if '-' in f:
        nova=str.replace(f,'-',' ')
    elif ',' in nova:
        nova=str.replace(f,',',' ')
    elif ':' in nova:
        nova=str.replace(f,':',' ')
    elif ';' in nova:
        nova=str.replace(f,';',' ')
    elif '.' in nova:
        nova=str.replace(f,'.',' ')
    return nova