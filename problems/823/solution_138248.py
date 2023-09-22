def faltante(lista_numeros):
    '''identifica qual número inteiro está faltando em uma lista com N números, numerados de 1 a N
    list -> int'''
    numero_faltante = 1
    while numero_faltante < len(lista_numeros):
        if numero_faltante not in lista_numeros:
            return numero_faltante
        else:
            numero_faltante += 1