def maiores(lista,n):
    """
    Função que dada uma lista de números inteiros e um número inteiro n,
    retorna outra lista, que contenha todos os números da lista original
    maiores que n.
    Parâmetro de Entrada: list, int
    Valor de Saida: list
    """
    list.append(lista,n)
    list.sort(lista)
    
    return lista[list.index(lista,n)+1:]