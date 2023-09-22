def retira_pontuacao(frase):
    """Função que substitui os caracteres de pontuação por espaço.
    str->str"""
    if ',' in frase:
        str.replace(frase,',',' ')
        return frase