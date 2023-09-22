def insere(lista_numero, n):
    """Função que, dada uma lista de números e um número n, insere o número na posição correta
    entrada: list, int
    saída: list"""
    
    list.append(lista_numero, n)
    list.sort(lista_numero)
    
    return lista_numero