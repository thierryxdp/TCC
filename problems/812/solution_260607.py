def retira_pontuacao(frase):
    """Recebe uma frase onde todos os caracteres de pontuação serão substituídos por espaço;
    str -> str"""
    frase_atualizada = frase.replace("_", " ").replace(",", " ").replace(":", " ")
    .replace(";", " ").replace(".", " ").replace("!", " ").replace("?", " ").replace("...", " ")