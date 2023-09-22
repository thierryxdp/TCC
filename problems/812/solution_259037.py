def retira_pontuacao(s):
    char_replace = ['!','?','.',',',';','-',':','...']
    s = str.replace(s,'.',' ')
    s = str.replace(s,'...',' ')
    s = str.replace(s,'!',' ')
    s = str.replace(s,'?',' ')
    s = str.replace(s,'-',' ')
    s = str.replace(s,',',' ')
    s = str.replace(s,';',' ')
    s = str.replace(s,':',' ')    
    return s