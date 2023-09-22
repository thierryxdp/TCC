def faltante(lista):
    '''função que recebe uma lista com numeros inteiros e retorna qual
    numero inteiro do intervalo está faltando.
    list -> int'''
    
    a= 0
    novalista = list.sort(lista)
    i= novalista[0]
    f= novalista[-1] + 1
    original = list(range(i,f))
    
    while original != lista:
        if novalista[a] != original[a]:
            erro = original[a]
        a += 1
        
    return erro