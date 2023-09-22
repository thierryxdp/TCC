def maiores(lista,n):
    """funcao que dada uma lista de numeros inteiros e um 
    numero inteiro n de entrada, retorna outra lista, que
    contenha todos os numeros da lista original maiores que 
    n ordenados em ordem crescente;
    list, int -> list"""
    
    lista2 = []
    for i in lista:
        if i>n:
            list.append (lista2,i)
    return lista2