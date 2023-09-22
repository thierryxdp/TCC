def retira_pontuacao(frase):
    string_retira= str.replace(frase,'-',' ')
    string_retira=str.replace(frase,',',' ')
    string_retira=str.replace(frase,'.',' ')
    string_retira=str.replace(frase,'!',' ')
    string_retira=str.replace(frase,'?',' ')
    return str.replace(string_retira)