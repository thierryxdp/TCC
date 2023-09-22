def conta_frases(texto):
    '''retorna o número de frases que aparecem em um texto, sendo cada frase contendo terminação em
    (./!/?/...).
    str -> int'''
    lista = str.split(texto,'./!/?/...')
    numero de frases = len(lista)
    return numero de frases