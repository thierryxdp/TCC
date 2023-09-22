def insere(lista_numero, n):
    """Função que insere um número inteiro na posição correta em uma lista ordenada, que é dada de valor de entrada
    entrada: list, int
    saída: list"""
    
    adicionado = list.append (lista_numero, n)
    b = list.sort(adicionado)
    
    return b