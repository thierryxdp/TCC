def retira_pontuacao(frase):
    """substitui todos os caracteres de pontuacao de uma frase por espaco
    str->str"""
    if '!' in frase:
        return str.replace(frase,'!',' ')
    elif ',' and '-' and '.' in frase:
        return str.replace(frase[0:34],',',' ')+str.replace(frase[34:44],'-',' ')+str.replace(frase[44:],'.',' ')