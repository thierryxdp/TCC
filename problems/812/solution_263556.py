def retira_pontuacao(texto):
    """Função que retorna a frase sem os caracteres de pontuação.
    str->str"""
    a=str.strip(texto,',!.')
    return a