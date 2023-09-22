def insere(lista_numero,n):
    '''Função que recebe uma lista ordenada crescente (lista_numero) de números inteiros e
    um número inteiro n e retorna incluindo n na posição correta (sem desordenar a lista).
    Entrada: list, int. Saída: list'''
    list.append(lista_numero,n) 
    list.sort(lista_numero) #ordena a lista
    return lista_numero