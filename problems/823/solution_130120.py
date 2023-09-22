def faltante(pecas):
    '''Função que dada uma lista com N - 1 inteiros numeros de 1 a N, descobre qual 
    numero está faltando
    list -> int'''
    contador = 1
    resultado = 0
    while contador <= len(lista):
        if contador not in lista:
            resultado += contador
        contador = lista[contador-1]+1
    if resultado == 0:
        resultado += len(lista)+1
    return resultado