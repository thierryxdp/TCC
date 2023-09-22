def retira_pontuacao(frase):
    """Função que dado uma frase retira todos os caracteres
    de pontuação
    str -> str"""
    frase = str.split(frase,"-")
    frase = str.split(frase,":")
    frase = str.split(frase, ";")
    frase = str.split(frase,".")
    frase = str.join(" ",frase)
    return frase