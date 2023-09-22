def lingua_p(frase):
    '''Retorna a palavra traduzida para a ligua do P
    str-->str'''
    lista=""
    for letra in frase:
        if letra in "aeiouAEIOUúáé":
            lista+=letra+"p"+letra
        else:
            lista+=letra
    return lista.lower()