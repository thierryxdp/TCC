def faltante(lista_pecas):
    """ retorna um numero inteiro  
    do intervalo N-1 que nao esta 
    na lista de entrada.
    list -> int"""
    lista_pecas.sort()
    i = 0
    acumulador = 1
    while i < len(lista_pecas):
        if acumulador in lista_pecas:
          acumulador += 1
        i += 1
    return acumulador