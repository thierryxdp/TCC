def maiores(lista):
    """dada uma lista de numeros inteiros e um numero
    inteiro n, retorna outra lista, contendo todos os 
    numeros maiores que n, em ordem crescente.
    list(int,int,...) -> list(int,int,...)"""
    
    list.append(lista,n)
    list.sort(lista)
    
    x = list.index(lista,n) + 1
    
    return lista[x:]