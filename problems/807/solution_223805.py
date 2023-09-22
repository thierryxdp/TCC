def conta_frases(texto):
    "Conta quantas frases um texto possui; string -> int"
    import re
    lista = re.split("[.!?]", texto)
    for frase in lista:
        if frase == "":
            lista.remove(frase)
    lista.remove("")
    tamanho = len(lista)
    return tamanho