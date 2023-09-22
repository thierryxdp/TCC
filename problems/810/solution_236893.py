def inverte(frase):
    """Funcoa que recebe uma frase e retorna o inverso dela sem letras maiusculas e pontuacao"""
    retira = frase.replace("-"," ").replace(","," ").replace(":"," ").replace(";"," ").replace("!"," ").replace("."," ").replace("?"," ")
    fraseMin = str.lower(retira)
    separaFrase = str.split(fraseMin)
    fraseInversa = separaFrase[::-1]
    return str.join(" ",fraseInversa)