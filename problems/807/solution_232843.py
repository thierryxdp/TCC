def conta_frases(frase):
    inter = str.count(frase,'?')
    escl = str.count(frase,'!')
    ponto = 0
    pontos = 0
    x = 1
    final = 0
    if frase[-1] == '.':
        final += 1
    while x < len(frase):
        if str.index(frase,'.',x) == str.index(frase,'.',str.index(frase,'.',x))-1:
            pontos +=1
            x += str.index(frase,'.',x)
        else:
            ponto += 1
            x += str.index(frase,'.',x)
    return inter+escl+ponto+pontos