def retira_pontuacao(frase):
    """retorna frase com todos os caracteres de pontuação substituidos por espaços.
    str->str"""    
    a= str.replace(frase,'.',' ')
    b= str.replace(a,',',' ')
    return str.replace(b,'-',' ')