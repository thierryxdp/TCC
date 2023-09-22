def insere(lista_numero, n):
    ''' Função que recebe um número (n) que entre em uma lista sem que
    sua ordenação altere.
    tipo de entrada:list e int
    tipo de saída: list'''
    
    adicionar = lista_numero.append(n)
    ordenar = list.sort(adicionar)
    return ordenar