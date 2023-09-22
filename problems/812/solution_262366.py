def retira_pontuacao(frase):
    """retorna a frase com os caracteres de pontuacao substituidos por espaco;
    str -> str"""
    pontuacao='.' or '!' or '?' or '-' or ',' or ':' or ';'
    return str.replace(frase,pontuacao,' ')