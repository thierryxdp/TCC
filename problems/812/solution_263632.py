def retira_pontuacao(frase):
    """Função que substitui os caracteres de pontuação por espaço.
    str->str"""
    if ',' and '.' in frase:
        str.replace(frase,',',' ') and str.replace(frase,'.',' ')
        return frase