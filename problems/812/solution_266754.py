def retira_pontuacao(frase):
    """funcao que dada uma frase, retorna a mesma substituindo os caracteres de pontuacao
    por espacos"""
    frase = str.replace(frase, "-", " ")
    frase = str.replace(frase, ",", " ")
    frase = str.replace(frase, ":", " ")
    frase = str.replace(frase, ";", " ")
    frase = str.replace(frase, ".", " ")
    return frase