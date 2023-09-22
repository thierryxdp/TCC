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

def inverte(frase):
    string_pontuacao = retira_pontuacao(frase)
    string = str.lower(string_pontuacao)
    return string[-1::-1]