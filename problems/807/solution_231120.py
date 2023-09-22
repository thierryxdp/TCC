def conta_frases(frases):
    ponto=str.count(frases,'.')
    exclamação=str.count(frases,'!')
    interrogação=str.count(frases,'?')
    reticências=str.count(frases,'...')
    letras=str.split(frases,' ')
    frases1=int(len(letras))-ponto-exclamação-interrogação-reticências
    return frases1