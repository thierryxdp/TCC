def maiores (lista:list[int], n:int)->list:
    '''Uma lista de números inteiros e um número inteiro(n)
    retorna uma outra lista contendo todos os números da 
    lista original maiores do que o n, em ordem crescente
    e ordenados.'''
    lista2=lista.copy()
    lista2.append(n)
    lista2.sort()
    posicao=lista2.index(n)
    maiores=lista2[posicao+1:]
    if n in maiores:
        quantidade=maiores.count(n)
        maiores=maiores[quantidade:]
    return maiores