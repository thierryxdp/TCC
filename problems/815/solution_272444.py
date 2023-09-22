def insere(lista_numero,n):
    """Função que, dada uma lista ordenada(crescente) de números inteiros e um número inteiro n, retorna a lista com n inclsuo na posição correta
    entrada: list, int
    saída: list"""
    lista_final=lista_numero+n
    return list.sort(lista_final)