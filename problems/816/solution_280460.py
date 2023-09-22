def maiores(lista_int,n):
    """função que retorna uma lista contendo todos os números maiores do que n da lista
    original, através dos dados de entrada 'lista_int' e 'n';
    Entrada: list, int
    Saída: list"""
    
    list.append(lista_int,n)
    list.sort(lista_int)
    x = list.index(lista_int,n)
    return lista_int[x+1:]