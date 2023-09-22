def maiores(lista_numero,n):
    '''Função que recebe uma lista de números inteiros e um número inteiro n.
    Retorna outra lista com todos os números da lista original maiores que n;
    list, int -> list'''
    nova_lista = [x for x in lista_numero if x > n]
    return nova_lista