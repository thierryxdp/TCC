def filtra_pares (numeros):
    """dada uma tupla de entrada contendo quatro números inteiros,
    retorna a mesma, no entanto contendo apenas elementos pares
    tuple --> tuple"""
    lista_numeros=list(numeros)
    lista_vazia=[]
    if lista_numeros[0]%2=0:
        lista_vazia.append(lista_numeros[0])
    if lista_numeros[1]%2=0:
        lista_vazia.append(lista_numeros[1])
    if lista_numeros[2]%2=0:
        lista_vazia.append(lista_numeros[2])
    if lista_numeros[3]%2=0:
        lista_vazia.append(lista_numeros[3])
    return lista_vazia