def retira_pontuacao(frase):
    """Funcao que retorna a frase em que todos os caracteres sao
    substituidos por um espaco
    str->str"""
    string_retira= str.replace(frase,'-',' ')
    string_retira= string_retira.replace(',',' ')
    string_retira= string_retira.replace('.',' ')
    string_retira= string_retira.replace('!',' ')
    string_retira= string_retira.replace('?',' ')
    return string_retira