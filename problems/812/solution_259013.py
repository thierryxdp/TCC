def retira_pontuacao(frase):
    """retorna a frase substituindo todos caracteres de pontuação por espacos em branco"""
    frase = str.split(frase, '!'';')
    frase = str.join(" ", frase)
    return frase