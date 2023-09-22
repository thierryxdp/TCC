def uppCons(frase):
    resposta=""
    for letra in frase:
        if letra not in {"a","e","i","o","u","á","é","í","ó","ú"}:
            resposta = resposta + letra.upper()
        else:
            resposta = resposta + letra
    return resposta