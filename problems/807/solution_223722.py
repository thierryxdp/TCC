def conta_frases(texto):
    "Conta quantas frases um texto possui; string -> int"
    lista = texto.split("." or "!" or "?")
    lista.del(".")
    tamanho = len(lista)
    return tamanho