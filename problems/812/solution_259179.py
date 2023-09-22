def retira_pontuacao(frase):
    """substitui todos os caracteres de pontuacao de uma frase por espaco
    str->str"""
    pontuacao='!' or ',' and '.' and '-' or '?' or '-' and '.' or '-' and '!' or '.' or ',' and '!'
    return str.replace(frase,pontuacao,' ')