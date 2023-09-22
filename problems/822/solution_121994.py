def repetidos(lista):
    '''Recebe uma lista de números e retorna o
    número de vezes que um elemento é igual ao anterior;
    list -> int'''
    anterior = ''
    contador = 0
    for numero in lista:
        if numero == anterior:
            contador += 1
        anterior = numero
    return contador