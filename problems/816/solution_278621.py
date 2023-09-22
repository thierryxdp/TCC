def maiores(lista,n):
    """Esta função recebe uma lista de números inteiros e um número inteiro e retorna outra lista com os números da outra lista que forem maiores que n
    list,int -> list"""
    maiores = []
    for i in lista:
    	if i > n:
            maiores.append(i)
            maiores.sort()
    return maiores