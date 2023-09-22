def lingua_p(palavra):
    contador = 0
    resultado = ''
    while contador < len(palavra):
        if palavra[contador] in 'a':
            resultado = resultado + 'apa'
        elif palavra[contador] in 'e':
            resultado = resultado + 'epe'
        elif palavra[contador] in 'i':
            resultado = resultado + 'ipi'
        elif palavra[contador] in 'o':
            resultado = resultado + 'opo'
        elif palavra[contador] in 'u':
            resultado = resultado + 'upu'
        elif palavra[contador] in 'á':
            resultado = resultado + 'ápá'
        elif palavra[contador] in 'é':
            resultado = resultado + 'épé'
        elif palavra[contador] in 'ú':
            resultado = resultado + 'úpú'
        else:
            resultado = resultado + palavra[contador]
        contador = contador + 1
    return resultado