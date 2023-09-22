def retira_pontuacao(frase):
    string_retira= str.replace(frase,'-',' ')
    string_retira=string_retira.replace(frase,',',' ')
    string_retira=string_retira.replace(frase,'.',' ')
    string_retira=string_retira.replace(frase,'!',' ')
    string_retira=string_retira.replace(frase,'?',' ')
    return string_retira