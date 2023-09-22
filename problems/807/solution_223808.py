def conta_frases(texto):
    "Conta quantas frases um texto possui; string -> int"
    import re
    lista = re.split("[.!?]", texto)
    for frase in lista:
        if frase == "":
            lista.remove(frase)
    for frase in lista:
        if frase == "":
            lista.remove(frase)
    tamanho = len(lista)
    return tamanho