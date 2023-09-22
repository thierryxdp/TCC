def retira_pontuacao(x):
     '-' in x:
        str.replace(x,'-',' ')
     '.' in x:
        str.replace(x,'.',' ')
     ';' in x:
        str.replace(x,';',' ')
     ':' in x:
        str.replace(x,':',' ')
     ',' in x:
        str.replace(x,',',' ')
     '!' in x:
        str.replace(x,'!',' ')
     '?' in x:
        str.replace(x,'?',' ')
    return x