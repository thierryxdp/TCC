def maiores(numeros: list[int],n: int,estritamente: bool = False) -> list[int]:
    '''recebe uma lista de numeros inteiros e um numero inteiro 'n' e 
    retorna outra lista com os numeros da lista original maior que 'n''''
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