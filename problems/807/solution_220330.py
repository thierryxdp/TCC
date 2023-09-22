def conta_frases(frase):
    lista_1 = frase.split(".")
    lista_2 = lista_1.split("!")
    lista_3 = lista_2.split("?")
    lista_4 = lista_3.split("...")
    return len(lista_4)