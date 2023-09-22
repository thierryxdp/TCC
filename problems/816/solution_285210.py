def maiores(lista,n):
    """ Essa função, ao receber uma lista de numeros inteiros e um valor n
    retorna uma lista com todos os valores acima de n em ordem crescente.
    lista,int-->lista"""
    
    list.append(lista,n)
    list.sort(lista)
    
    lista_final = lista[list.index(lista,n)+1:]
    
    return lista_final