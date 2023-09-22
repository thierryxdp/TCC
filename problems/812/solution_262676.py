def retira_pontuacao(frase):
    """Função, que dada uma frase, retorna a frase onde todos os caracteres de pontuação, foram substituídos por espaço."""
    """str->str"""
    for x in ".!?,;:-":
        frase = frase.replace(x, " ")
    return frase