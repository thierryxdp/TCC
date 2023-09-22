def maiores(lista, n):
    """Função que dada uma lista de números inteiros, e um número inteiro 
       n, retorna uma nova lista com todos on números maiores que n
       
       Parameters:
       lista: Lista de números inteiros
       n: Número que usaremos de base para formar a nova lista
       
       Returns:
       Retorna uma nova lista com todos os números maiores que n
       list, int -> list
       """
    list.append(lista,n)
    list.sort(lista)
    posicao=list.index(lista,n)
    return lista[posicao+1:]