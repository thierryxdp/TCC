def lingua_p(palavra):
    tradutor = []
    contador = 0
    for letra in list (palavra):
        if letra in "aáeéiíoóuú":
            tradutor.append(letra + "p" + letra)
        else:
            tradutor.append(letra)
    return "".join(tradutor)