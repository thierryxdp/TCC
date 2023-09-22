def faltante(lista):
    
    ''' dado uma lista de número faltando um elemento sequencial,
    retorna qual elemento está faltando 
    list --> int 
    '''
    i = 1
    j = len(lista)-1
    while i != len(lista) + 2:
        if i not in lista and i < lista[j]:
            return i
        if i not in lista and i > lista[j]:
            return i
        if i in lista:
            i += 1