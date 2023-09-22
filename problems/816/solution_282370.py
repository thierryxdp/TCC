def maiores (lista: list, n: int)-> list:
    '''Dada uma lista de números inteiros e um número inteiro n, 
    retorna outra lista que contenha todos os números da lista 
    original em ordem crescente'''
    copialista= lista.copy()
    copialista.append(n)
    copialista.sort()
    posicao= copialista.index(n)
    maiores= copalista[posicao + 1:]
    if n in maiores:
        quant= maiores.count(n)
        maiores = maiores[quant:]
    return maiores