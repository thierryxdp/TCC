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
        if x < len(frase) and frase[x] == '.' and frase[x+1] == '.':
          	pontos +=1
            x +=3
        elif frase[x] == '.':
            ponto+=1
            x+=1
        else:
            x+=1
    return inter+escl+ponto+pontos