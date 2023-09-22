def maiores(lista, n):
    """Função que compara os elementos de uma lista com um inteiro n
    e retorna, em ordem crescente, os numeros maiores que n
    list,int --> list"""
    list.sort(lista)
    ret=[]
    for elemento in lista:
        if( elemento > n ):
            list.append(ret, elemento)
    return ret