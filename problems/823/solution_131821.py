def faltante(lista):
    
    '''recebe uma lista com uma quantidade de elementos N-1 inteiros numerados de 1 a N e retorna qual o número está faltando no intervalo dado.
    list -> int'''    
    
    list.sort (lista)
    contador = 2
    
    while 1 in lista and len(lista)<lista[-1]:
        if contador not in lista:
            return contador
        contador = contador + 1

    if 1 not in lista:
        return 1
    
    if 1 in lista and len(lista) == lista[-1]:
        return lista[-1] + 1