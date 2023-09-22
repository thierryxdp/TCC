def faltante(lista):
    '''Função que dada uma lista de numeros de 1 a n retorne qual o numero
    deste intervalo está faltando
    list -> int'''
    i= 0
    cont= 1
    while i <= len(lista): 
        if i == len(lista):
            return len(lista)
        if lista[i] != cont:
            return lista[i] - 1 
        cont= cont + 1
        i= i + 1