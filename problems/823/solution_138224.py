def faltante(lista):
    ''' Função onde mostra a quantidade de peças do 
    quebra cabeça que falta.
    list -> int'''
    
    i = 1
    x = len (lista) - 1
    
    while i != len (lista) + 2:
        if i not in lista and i < lista[x]:
            return i
        if i not in lista and i > lista[x]:
            return i
        if i in lista:
            i += 1