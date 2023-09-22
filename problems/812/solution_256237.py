def retira_pontuacao(frase):
    string = str.replace(frase,'!',' ')
    string = str.replace(string,'?',' ')
    string = str.replace(string,'...',' ')
    string = str.replace(string,'.',' ')
    string = str.replace(string,'-',' ')
    string = str.replace(string,',',' ')
    string = str.replace(string,':',' ')
    string = str.replace(string,';',' ')
    return string