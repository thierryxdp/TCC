def inverte (frase):
    """Calcula e retorna a variavel de entrada frase 
    na ordem inversa, sem letra maiuscula e sem
    pontuacao; str --> str"""
    frase.replace("-","")
    frase.replace("!","")
    frase.replace(";","")
    frase.replace(",","")
    frase.replace(".","")
    frase.replace(":","")
    frase.replace("?","")
    frase.replace("!","")
    frase.lower
    return frase[::-1]