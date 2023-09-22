def retira_pontuacao(frase):
    """retorna a frase com os caracteres de pontuacao substituidos por espaco;
    str -> str"""
    pontuacao='.' and '!' and '?' and '-' and ',' and ':' and ';'
    return str.replace(frase,pontuacao,' ')