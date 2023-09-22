def faltante(lista:list) ->int:
    ''''''
    n = 0
    i = 0
   
    while i <= len(lista):
        if i not in lista:
            n = i  
    	i = i + 1      
    if n == 0:
        n = len(lista) + 1
    return n