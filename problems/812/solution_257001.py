def retira_pontuacao(frase):
    string_retira= str.replace(frase,'-',' ')
    string_retira=str.replace(frase,',',' ')
    string_retira=str.replace(frase,'.',' ')
    string_retira=str.replace(frase,'!',' ')
    string_retira=str.replace(frase,'?',' ')
    return str.upper(string_retira)