from random import randrange

def geraIndiceAleatorio(vetor):
  return randrange(len(vetor))

def pegaRandom(vetor,k=1):
  if k==1:
    return vetor[geraIndiceAleatorio(vetor)]
  else:
    retorno = []
    vetor2 = vetor[:]

    for j in range(k):
      indice = geraIndiceAleatorio(vetor2)
      retorno.append(vetor2[indice])
      vetor2.pop(indice)

    return retorno