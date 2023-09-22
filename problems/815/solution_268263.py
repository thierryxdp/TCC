def insere(lista_numero:list, n:int) -> list:
    """Dada uma lista de números inteiros em ordem crescente, incluir n
       na posição em que continue crescente
       
       Parameters:
       lista_numero: lista de números inteiros em ordem crescente
       n: número a ser inserido na lista
       
       Returns:
       lista de números com o n incluso na ordem crescente
    """
    lista_nova = list.append(lista_numero,n)
    return  list.sort(lista_nova)