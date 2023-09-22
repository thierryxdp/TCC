def maiores(numeros: list[int],n: int,estritamente: bool = False) -> list[int]:
    '''Retorna uma lista com todos os numeros da lista
       de entrada que são maiores que n'''
    numerosCopia = numeros.copy()
    numerosCopia.append(n)
    numerosCopia.sort()
    posicaoN = numerosCopia.index(n)
    numerosMaiores = numerosCopia[posicaoN+1:]
    if estritamente:
         if n in numerosMaiores:
             quantidade = numerosMaiores.count(n)
             numerosMaiores = numerosMaiores[quantidade:]
    else:
        pass
        
    return numerosMaiores


def acima_da_media(notas: list[float]) -> list[float]:
    '''Retorna as notas que estão acima da média'''
    media = sum(notas)/len(notas)
    acimaDaMedia = maiores (notas, media, True)
    return acimaDaMedia