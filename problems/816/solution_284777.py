def maiores(listadenumerosinteiros,n):
    """Funcao  que recebe uma lista de numeros inteiros e um numero inteiro n, retorna uma lista com os numeros maiores que n e em ordem cresecente. list,int=>list"""
    list.insert(listadenumerosinteiros,0,n)
    list.sort(listadenumerosinteiros)
    return listadenumerosinteiros[list.index(listadenumerosinteiros,n)+1:]