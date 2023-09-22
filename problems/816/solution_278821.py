def maiores(lista,n):
    """Função que dado uma lista de números inteiros e um número interino n,  retorna uma lista nova que  contenha todos os números da lista original maiores que n
       Parâmetros: list,int -> list"""
    nova_lista = lista[0]
    n = lista[1]
    nova_lista.append(n)
    if max(nova_lista) == n:
        return []
    else:
        lista_decre = sorted(nova_lista,reverse=True)
        index_n = lista_decre.index(n)
        return sorted(lista_decre[:index_n]