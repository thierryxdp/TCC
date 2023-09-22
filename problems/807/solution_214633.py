def conta_frases(texto):
    '''função que dado um texto em string, retorna a quantidade de frases
       contidas neste texto. str -> int'''
    t = []
    if len(str.split(texto,'. ')) >= 2:
        t = t + len(str.split(texto,'. '))
    if len(str.split(texto,'... ')) >= 2:
        t = t + len(str.split(texto,'... ')) - 1
    if len(str.split(texto,'! ')) >= 2:
        t = t + len(str.split(texto,'! ')) -1 
    if len(str.split(texto,'? ')) >= 2:
        t = t + len(str.split(texto,'? ')) - 1
    return t