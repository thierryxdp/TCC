def conta_frases(frase):
    inter = str.count(frase,'?')
    escl = str.count(frase,'!')
    ponto = 0
    pontos = 0
    x = 0
    final = 0
    if frase[-1] == '.':
        final += 1
    while x < str.count(frase,'.'):
        if str.index(frase,'.',x) == str.index(frase,'.',x+1)+1:
            pontos +=1
            x += 2
        else:
            ponto += 1
            x +=1
    return inter+escl+ponto+pontos