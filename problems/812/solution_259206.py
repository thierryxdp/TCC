def retira_pontuacao(frase):
    """dada uma frase substitui as pontuaçoes desta por espaços vazios
    str->str"""
    if '!' in frase:
        return str.replace(frase,'!',' ')