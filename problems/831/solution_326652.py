def lingua_p(palavra):
    resultado=''
    for letra in palavra.lower():
        if letra in 'âàáãaêèéeîìíiôòóõoûùúu':
            resultado+= letra+'p'+letra
        else:
            resultado+=letra
        
    return resultado