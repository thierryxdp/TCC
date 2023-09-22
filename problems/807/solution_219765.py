def conta_frases(texto):
    #essa função conta a quantidade de frases em uma string
    x=texto.replace("!"," .")
    x=texto.replace("?", ".")
    x=texto.replace("."," .")
    x=texto.split(".")
    y=len (x)
    return y