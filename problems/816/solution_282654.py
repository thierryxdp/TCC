def maiores(lista_inteiros,n):
    '''funcao que retorna uma lista ordenada em ordem crescente apenas com
    numeros da lista de entrada que sejam maiores que o numero n
    list(int),int -> list(int)'''
    list.append(lista_inteiros,n)
    list.sort(lista_inteiros)
    indice_n = list.index(lista_inteiros,n)
    return lista_inteiros[indice_n+1:]