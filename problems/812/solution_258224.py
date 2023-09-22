def retira_pontuacao(frase):
    """retorna frase com todos os caracteres de pontuação substituidos por espaços.
    str->str"""    
    a= str.replace(frase,'.',' ')
    return str.replace(a,',',' ')