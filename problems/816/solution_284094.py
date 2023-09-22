def maiores(lista,n):
    """
    funcao que dada uma lista de numeros inteiros e 
    um numero inteiro n, retorna outra lista que contenha
    todos os numeros dessa lista original
    : lista --> lista 
    """
    numeros_maiores = [ x for x in lista if x > n ]
    list.sort(numeros_maiores)
    return numeros_maiores