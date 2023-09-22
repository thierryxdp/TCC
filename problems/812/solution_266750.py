def retira_pontuacao(frase):
    """funcao que dada uma frase, retorna a mesma substituindo os caracteres de pontuacao
    por espacos"""
    frase = str.split(frase, "-")
    frase = str.split(frase, ",")
    frase = str.split(frase, ":")
    frase = str.split(frase, ".")
    frase = str.split(frase, ";")
    return frase