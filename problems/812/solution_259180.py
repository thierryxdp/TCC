def retira_pontuacao(frase):
    """substitui todos os caracteres de pontuacao de uma frase por espaco
    str->str"""
    pontuacao='!' or ',' or '.' or '-' or '?' 
    return str.replace(frase,pontuacao,' ')