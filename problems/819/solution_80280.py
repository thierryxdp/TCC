def pegaRandom(vetor,k=1):
    n = len(vetor)
    i = randrange(n)
    retorno = vetor[i]
    if k==1:
        return retorno
    else:
        vetor2 = list(vetor)
        vetor2.pop(i)
        return retorno, pegaRandom(vetor2,k-1)