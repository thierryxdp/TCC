def insere(lista_numero, n):
    """Função que insere um número inteiro na posição correta em uma lista ordenada, que é dada de valor de entrada
    entrada: list, int
    saída: list"""
    
    lista = [lista_numero]
    a = list.append (lista, n)
    b = list.sort(a)
    
    return b