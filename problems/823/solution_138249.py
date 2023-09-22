def faltante(lista_numeros):
    '''identifica qual número inteiro está faltando em uma lista com N números, numerados de 1 a N
    list -> int'''
    numero_faltante = 0
    while numero_faltante < len(lista_numeros):
        numero_faltante = numero_faltante + 1
        if numero_faltante not in lista_numeros:
            return numero_faltante
    return numero_faltante + 1