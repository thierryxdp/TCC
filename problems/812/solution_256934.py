def retira_pontuacao(frase):
    """Funcao que dada uma frase, retorna a frase sem os caracteres de pontuacao.
    str->str"""
    frase=str.punctuation
    s=str.replace(frase)
    return s