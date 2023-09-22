def conta_frases(texto):
    "Conta quantas frases um texto possui; string -> int"
    lista = texto.split("." or "!" or "?")
    for frase in lista:
        if frase == "":
            lista.remove(frase)
    lista.remove("")
    tamanho = len(lista)
    return lista