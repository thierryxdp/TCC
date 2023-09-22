def faltante(lista:list) ->int:
    ''''''
    n = 0
    i = 0
    while i <= len(lista):
        if i not in lista:
            n = i
    	i = i + 1        
    return n