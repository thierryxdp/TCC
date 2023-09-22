def repetidos(list_n):
    '''Função que recebe uma lista de numeros e retorna quantas vezes um numero foi igual ao numero anterior.
    list -> str'''
    i=0
    repetidos=0
    while i<len(list_n):
        if list_n[i] == list_n [i+1]:
            repetidos = repetidos +1
        i=i+1
        if len(list_n) == 2 and list_n == list_n [i]:
            repetidos = 1
    return repetidos