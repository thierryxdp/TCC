def maiores(lista,n):
    """Essa funcao recebe uma lista de numeros inteiros e um numero inteiro e retorna uma nova lista com
    todos os numeros da lista original que sao maiores que o numero inteiro dado;
    list, int -> list
    """
    list.append(lista,n)
    list.sort(lista)
    nova_lista = lista[list.index(lista,n)+1:]
    return nova_lista