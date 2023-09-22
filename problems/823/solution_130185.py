def faltante (list):
    ''' Função que dado uma lista numerada de 1 a N inteiros, retorna qual numero da sequencia está faltando.
    list -> int'''
    i=0
    list.sort()
    while list [i-] == i:
        i + 1
        if i > len(list):
            return i 
    return i