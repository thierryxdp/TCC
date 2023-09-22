def repetidos(numeros):
    '''funcao que recebe uma lista de numeros e retorna o numero de vezes que o elemento da lista é igual ao elemento anteiror
    list->int'''
    i = 0
    acumul = 0
    while i < len(numeros):
        if numeros[i] == numeros [i-1]:
            acumul = acumul +1
        i = i+1
    return acumul