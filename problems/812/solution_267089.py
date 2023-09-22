def retira_pontuacao(frase):
    """recebe uma string com uma frase e retorna uma string com a mesma frase
    com seus caracteres de pontuação substituidos por espaço"""
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
    if "!" in lista:
        lista[list.index(lista,"!")] = " "
    if "?" in lista:
        lista[list.index(lista,"?")] = " "

    lista_final = "".join(lista)
    
    return lista_final