def lingua_p(palavra):
    resultado=''
    for letra in palavra.lower():
        if letra in 'ÂÃÁÀAÊÈÉEÎÌÍIÔÕÒÓOÛÙÚUâàáãaêèéeîìíiôòóõoûùúu':
            palavra+= letra+'p'+palavra
        else:
            resultado+=letra
        
    return resultado