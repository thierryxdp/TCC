def inverte(frase):

    """Função que dada uma frase retorna uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação.
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