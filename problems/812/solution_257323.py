def retira_pontuacao(frase):
    """Função que, dada uma frase, retorna a frase onde todos os caracteres de pontuação tenham sido substituídos por espaço.
    str -> str"""

    
    frase = frase.split(".")
    frase = str.join(" ",frase)

    frase = frase.split("!")
    frase = str.join(" ",frase)

    frase = frase.split("?")
    frase = str.join(" ",frase)

    frase = frase.split(":")
    frase = str.join(" ",frase)

    frase = frase.split(",")
    frase = str.join(" ",frase)

    frase = frase.split(";")
    frase = str.join(" ",frase)

    frase = frase.split("-")
    frase = str.join(" ",frase)
    
    return frase