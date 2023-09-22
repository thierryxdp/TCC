def retira_pontuacao(frase):
    """Retorna a frase com os caracteres de pontuação substituidos por espaço;
    str->str"""
    return frase.replace(".,?!-:;","")