def maiores(lInt,n):
    '''Retorna uma lista com os inteiros da lista de entrada
       maiores que o número n, também de entrada, ordenados 
       em ordem crescente;
       list, int -> int'''
    lInt.append(n)
    lInt.sort()
    return lInt[lInt.index(n)+1:]