def conta_frases(x):
    "recebe texto e retorna o numero de frase no texto, str --> int"
    pontuacao=['!','?','.']
    texto= x.split()
    cont= 0
    for pal in texto:
        for pont in pontuacao:
            if pont in pal:
                cont+=1
    return cont