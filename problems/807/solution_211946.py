def conta_frase(texto):
    dwight = []
    texto = texto.strip()

    tres_pontinhos = texto.split('...')
    dwight.append(tres_pontinhos)

    ex = texto.split('!')
    dwight.append(ex)

    inter = texto.split('?')
    dwight.append(inter)

    ponto = texto.split('.')
    dwight.append(ponto)

    return len(dwight)