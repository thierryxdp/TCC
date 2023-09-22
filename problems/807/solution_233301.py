def conta_frases(texto):
    texto = texto.replace("...","#")
    texto = texto.replace(".","#")
    texto = texto.replace("?","#")
    texto = texto.replace("!","#")
    lista=texto.split("#")
    return len(lista)-1