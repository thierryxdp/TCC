def lingua_p(frase):
    lista=""
    for letra in frase:
        if letra in "aeiouAEIOUúáé":
            lista+=letra+"p"+letra
        else:
            lista+=letra
    return lista.lower()