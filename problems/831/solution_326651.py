def lingua_p(palavra):
    resultado=''
    for letra in palavra.lower():
        if letra in 'âàáãaêèéeîìíiôòóõoûùúu':
            resultado+= letra+'p'+palavra
        else:
            resultado+=letra
        
    return resultado