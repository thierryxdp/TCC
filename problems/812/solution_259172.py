def retira_pontuacao(frase):
    """substitui todos os caracteres de pontuacao de uma frase por espaco
    str->str"""
    if '!' in frase:
        return str.replace(frase,'!',' ')
    elif ',' and '.' in frase:
        return str.replace(frase,',' and '.',' ')