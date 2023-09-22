def conta_frases(texto):
    contador = []

    pontinhos = str.find(texto, '...')
    if(pontinhos > 0):
        a = str.count(texto, '...')
        contador.append(a)

    ex = str.find(texto, '!')
    if (ex > 0):
        contador.append(str.count(texto, '!'))

    inter = str.find(texto, '?')
    if (inter > 0):
        contador.append(str.count(texto, '?'))


    ponto = str.find(texto, '.')
    if (ponto > 0):
        contador.append(str.count(texto, '.'))





    return len(contador)