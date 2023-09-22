def conta_frases(frase):
    inter = str.count(frase,'?')
    escl = str.count(frase,'!')
    ponto = 0
    pontos = 0
    x = 1
    while ponto < str.count(frase,'.'):
        if str.find(frase,'.',x) == str.find(frase,'.',x+1):
            pontos +=1
            x += 3
        else:
            ponto += 1
            x +=1
    return inter+escl+ponto+pontos+final