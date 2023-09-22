def maiores(lista,n):
    """Função que recebe um parâmetro (lista) de numeros inteiros, e (n) valor inteiro
    e retorna uma segunda lista com todos os números maiores que n.
    list, int -> list"""
    
    list.append(lista,n)
    list.sort(lista)
    
    indice = list.index(lista,n)
    
    del lista[0:n]

    return lista