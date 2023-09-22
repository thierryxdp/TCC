def faltante (lista):
    ''' Função que dado uma lista numerada de 1 a N inteiros, retorna qual numero da sequencia está faltando.
    list -> int'''
    i=1
    lista.sort()
    while lista [i-1] == i:
        i += 1
        if i > len(lista):
            return i 
    return i