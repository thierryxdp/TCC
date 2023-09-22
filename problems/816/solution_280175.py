def maiores(lista = list, n = int) -> list:
    """Função que recebe uma lista de números inteiros (lista) e um número inteiro (n), e então 
    retorna outra lista, que contém todos os números da lista original maiores que n."""
    nova_lista = lista + [n]
    nova_lista = sorted(nova_lista)
    x = nova_lista.index(n)
    nova_lista = nova_lista[x:]
    return nova_lista