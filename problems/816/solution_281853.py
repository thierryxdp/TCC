def maiores(lista,n):
    """dada uma lista de numeros inteiros e um numero 
    inteiro n, retorna outra lista, contendo todos os 
    numeros da lista original maiores que n, ordenados
    em ordem crescente.
    list(int,int,...),int -> list"""
    a=0
    while a-1<len(lista):
        if int(lista[a])<=n:
            del lista[a]
        a+=1
    list.sort(lista)
    
    return lista