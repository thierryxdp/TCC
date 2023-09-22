def retira_pontuacao(frase):
    """funcao que dada uma frase, retorna a mesma substituindo os caracteres de pontuacao
    por espacos"""
    caracteres = ["-",",",":",".",";"]
    frase = str.split(frase, caracteres)
    frase = str.join(" ", frase)
    return frase