def faltante(L):
    """ recebe uma lista de tamanho n-1, que contém números inteiros não repetidos
    de 1 a N, e retorna qual inteiro está faltando nesta lista (pertence ao intervalo
    mas não está presente na lista.
    list-> int """
	numero=1
    
    while numero in L:
        numero+=1
    return numero