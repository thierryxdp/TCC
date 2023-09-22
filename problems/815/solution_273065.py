def insere(lista_numero,n):
    """Função que dada uma lista ordenada crescente de números inteiros e um número inteiro n;
    inclua n na posição de forma que a lista continue ordenada;
    list, int -> list"""
    listan = [n]
    novo_lista_numero = lista_numero + listan
    return (sorted([novo_lista_numero]))