def retira_pontuacao(frase):
    """Função que retorna uma frase onde todos os caracteres
    de pontuação tenham sido substituidos por espaço"""
    frase = str.split(frase,",")
    frase = str.join(" ", frase)
    return frase