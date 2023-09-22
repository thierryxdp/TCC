def retira_pontuacao(frase):
    """Reorna a frase sem os caracteres de pontuacao.str-->str."""
    return str.replace(frase,"!"," ") + str.replace(frase,"."," ")