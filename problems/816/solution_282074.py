def maiores(numeros, n):
    """ Dada uma lista de números inteiros e um número inteiro n, retorna outra lista que contenha todos os números da lista original 
    maiores que n, ordenados em ordem crescente
    list, int -> list """
    saida = numeros[:]
    saida.append(n)
    saida.sort()
    saida = saida[saida.index(n+1):]
    return saida