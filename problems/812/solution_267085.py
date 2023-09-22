def retira_pontuação(frase):
    lista = []
    lista[:] = frase

    if "-" in lista:
        lista[list.index(lista,"-")] = " "
    if "," in lista:
        lista[list.index(lista,",")] = " "
    if ":" in lista:
        lista[list.index(lista,":")] = " "
    if ";" in lista:
        lista[list.index(lista,";")] = " "
    if "." in lista:
        lista[list.index(lista,".")] = " "

    lista_final = "".join(lista)
    
    return lista_final