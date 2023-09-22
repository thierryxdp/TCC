def inverte(frase):

    """Função que, dada uma frase, retorna a frase onde todos os caracteres de pontuação tenham sido substituídos por espaço.
    str -> str"""

    frase = frase.lower()
    
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

    frase = frase.split()
    frase = frase[::-1]
    frase = str.join(" ", frase)

    
    return frase