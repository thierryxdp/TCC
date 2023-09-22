def retira_pontuacao(s):
    char = ['!','?','.',',',';','-',':','...']
    s = str.replace(s,'.',' ')
    s = str.replace(s,'...',' ')
    s = str.replace(s,'!',' ')
    s = str.replace(s,'?',' ')
    s = str.replace(s,'-',' ')
    s = str.replace(s,',',' ')
    s = str.replace(s,';',' ')
    s = str.replace(s,':',' ')    
    return s