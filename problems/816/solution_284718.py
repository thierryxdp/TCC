def maiores(numeros,n):
    """Retorna uma lista com todos os números da lista
       fornecida maiores que 'n' em ordem crescente.
       list,int -> list"""
    list.append(numeros,n)
    list.sort(numeros)
    posicao = list.index(numeros,n)
    return numeros[posicao:]