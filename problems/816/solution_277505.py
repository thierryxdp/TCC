def maiores(lista_inteiros:list, n:int) -> list:
    """Dada uma lista de números inteiros, elimina todos os elementos 
       menos que n
    
       Parameters:
       lista_numero: lista de números interios
       n: número referencial
       
       Returns:
       lista de números maiores que n
    """
    list.append(lista_inteiros, n)
    list.sort(lista_inteiros)
    indice = list.index(lista_inteiros, n)
    
    return lista_inteiros[indice:]