def freq_palavras(frase):
    dicionario = {}
    contador = 0
    a = ''
    for letra in frase:
        if letra != ' ':
            soma = a+letra
            a = soma
        if letra == ' ':
            a = ''
            contador = 0
            for m in dicionario:
                if (m == soma):
                    dicionario[soma] += 1
                    contador += 1
            if contador == 0:
                dicionario[soma] = 1
    contador = 0
    for m in dicionario:
        if (m == soma):
            dicionario[m] += 1
            contador += 1
    if contador == 0:
        dicionario[soma] = 1
    return{dicionario}