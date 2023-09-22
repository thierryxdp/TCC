def retira_pontuacao(frase):
    """Essa função retira todos os caracteres de pontuação e substitui por espaço"""
    frase = frase.replace("-", " ")
    frase = frase.replace(",", " ")
    frase = frase.replace(":", " ")
    frase = frase.replace(";", " ")
    frase = frase.replace(".", " ")
    return frase