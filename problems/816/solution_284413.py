def maiores(lista_numero, n):
    """Função que dado como parâmetros uma lista de números inteiros e um número inteiro, retorna uma lista com os números maiores que "n" em ordem
    crescente. Entrada - > list,int; Saída -> list"""
    lista = lista_numero
    list.append(lista, n)
    list.sort(lista)
    
    indice = list.index(lista, n)
    
    return lista[indice+1:]