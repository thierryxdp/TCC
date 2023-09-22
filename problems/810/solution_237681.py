def inverte(frase):
    """Inverte uma frase e retorna outra frase sem letras letras maiúscula e pontuações"""
    frase = frase.replace("!","")
    frase = frase.replace("?","")
    frase = frase.replace("-","")
    frase = frase.replace(",","")
    frase = frase.replace(":","")
    frase = frase.replace(";","")
    frase = frase.replace(".","")
    frase1 = str.split(frase)
    frase2 = str.join(" ",frase1[::-1])
    return str.lower(frase2)