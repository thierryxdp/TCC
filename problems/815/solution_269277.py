def insere(lista_numero, n):
    """Função que, dada uma lista de números e um número n, insere o número na posição correta
    entrada: list, int
    saída: list"""
    
    lista_nova = list.append(lista_numero, n)
    ordenada = list.sort(lista_nova)
    
    return ordenada