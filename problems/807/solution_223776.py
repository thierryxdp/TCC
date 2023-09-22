def conta_frases(texto):
    "Conta quantas frases um texto possui; string -> int"
    lista = texto.split("." and "!" and "?")
    for frase in lista:
        if frase == "":
            lista.remove(frase)
    tamanho = len(lista)
    return tamanho