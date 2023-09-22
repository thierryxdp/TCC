def conta_frases(texto):
    texto = texto.replace("...","#")
    print (texto)
    texto = texto.replace(".","#")
    print (texto)
    texto = texto.replace("?","#")
    print (texto)
    texto = texto.replace("!","#")
    print (texto)
    lista=texto.split("#")
    print (lista)
    return len(lista)-1

conta_frases('Socorro DEus. Quero dormir!')