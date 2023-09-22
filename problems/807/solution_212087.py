def conta_frases(texto):
    '''esta funcao conta numero de frases presente em um texto
    str -> int'''
    contador = 0
    contador_ret = 0
    for i in texto:
        if i in '.!?':
            contador += 1
    lista = str.split(texto, ' ')
    for i in lista:
        if '...' in i:
            contador_ret += 1
    return contador - (contador_ret * 2)