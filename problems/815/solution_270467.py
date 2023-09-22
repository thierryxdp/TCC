def insere(lista, n):
    ''' Função que recebe um número (n) que entre em uma lista sem que
    sua ordenação altere.
    tipo de entrada:list e int
    tipo de saída: list'''
    
    lista.append(n)
    return lista.sort()