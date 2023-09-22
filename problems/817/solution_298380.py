def acima_da_media(notas: list[float]) -> list[float]:
    '''Retorna uma lista com todos os numeros da lista
       de entrada que são maiores que n'''
    media= sum(notas)/len(notas)
    copianotas= notas.copy()
    copianotas.append(media)
    copianotas.sort()
    posicaoN= copianotas.index(n)
    numerosMaiores = copianotas[posicaoN+1:]
    if media:
        if n in copianotas:
            quantidade = numerosMaiores.count(n)
            numerosMaiores = numerosMaiores[quantidade:]
    else:
        pass 
    return numerosMaiores