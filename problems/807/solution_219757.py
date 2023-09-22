def conta_frases(texto):
    #essa função conta a quantidade de frases em uma string
    x=texto.replace("!"," .")
    x=texto.replace("?", ".")
    x=texto.replace("..."," .")
    y=texto.split(".")
    x=len (frase)
    return x