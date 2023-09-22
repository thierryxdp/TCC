def lingua_p(palavra):
    indice=0
    while indice < len(palavra):
        if palavra[indice] in "AEIOUaeiou":
            palavra[indice]=palavra[indice]+"p"+palavra[indice]
        indice=indice+1
    return palavra