def conta_frases(frase):
    ''' '''
    pontuacao=['!','?','.','...']
    difenrenca= pontuacao[2] != pontuacao[3]
    pontuacao1= frase.count(pontuacao[0])
    pontuacao2= frase.count(pontuacao[1])
    pontuacao3= frase.count(pontuacao[2])
    pontuacao4= frase.count(pontuacao[3])
    return pontuacao1+pontuacao2+pontuacao3+pontuacao4