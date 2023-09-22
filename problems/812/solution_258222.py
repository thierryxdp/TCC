def retira_pontuacao(frase):
    """retorna frase com todos os caracteres de pontuação substituidos por espaços.
    str->str"""    
    return str.replace(frase,'.',' ')