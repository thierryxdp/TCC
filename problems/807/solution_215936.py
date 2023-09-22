#--------EXERCICIO 2-------

def conta_frases (texto):
    '''conta quantas frases tem no texto
       str -> int'''

    pontoReticencias = str.count(texto,'...')
    pontoExclamacao = str.count(texto,'!')
    pontoFinal = str.count(texto,'.')
    pontoPergunta = str.count(texto,'?')
    
    if pontoReticencias != 0:
        pontoFinal -= 3*pontoReticencias
    
    totalpontos = pontoExclamacao + pontoFinal + pontoReticencias + pontoPergunta

    return totalpontos