def conta_frase(texto):
    dwight = []
    texto = texto.strip()

    if '...' in texto:
        pontinhos = texto.split('...')
        dwight.append(pontinhos)
    else:
        ()

    ex = texto.split('!')
    dwight.append(ex)

    inter = texto.split('?')
    dwight.append(inter)


    ponto = texto.split('.')
    dwight.append(ponto)

    return len(dwight)