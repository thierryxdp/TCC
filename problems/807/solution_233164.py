def conta_frases(x):
    "recebe texto e retorna o numero de frase no texto"
    pontuacao=['!','?','.']
    texto= x.split()
    cont= 0
    for lac_pal in texto:
        for lac_pont in pontuacao:
            if lac_pont in lac_pal:
                cont+=1
    return cont