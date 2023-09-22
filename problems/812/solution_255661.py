def retira_pontuacao(frase):
    """Retorna a frase dado sem caracteres de pontuacao e com espaco no lugar.
    str->str"""
    return str.replace(str.replace(str.replace(str.replace(frase,'!',' '),',',' '),'.',' '),'?',' ')