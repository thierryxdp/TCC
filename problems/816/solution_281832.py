def maiores(lista,n):
    """dada uma lista de numeros inteiros e um numero 
    inteiro n, retorna outra lista, contendo todos os 
    numeros da lista original maiores que n, ordenados
    em ordem crescente.
    list(int,int,...),int -> list"""
    a=0
    while a<len(lista):
        if lista[a]<=n:
            del lista[a]
        i+=1
    return list.sort(lista)