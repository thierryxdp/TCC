def conta_frases(texto):
   #recebe um texto e corta em frases entre os sinais
   #string -> list

    ponto= str.count(texto,'.')
    ex = str.count(texto, '!')
    inter = str.count(texto, '?')
    pontinhos = str.count(texto, '...')
    pontinhos = pontinhos -2

    sinais = ponto+ex+inter+pontinhos
    lista_range = list(range(sinais))

    return len(lista_range)