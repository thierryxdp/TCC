def insere (lista_numero = list, n = int) -> list:
    """Função que recebe uma lista ordenada crescente de números inteiros(lista_numero) e um 
    número inteiro(n), e então, inclui n na posição correta, de maneira que a lista continue 
    ordenada."""
    nova_lista = lista_numero + [n]
    return list.sort(nova_lista)