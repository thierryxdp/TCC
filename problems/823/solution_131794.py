def faltante(lista:list) ->int:
    '''Recebe uma lista enumerada de 1 a N, com N-1 elementos 
    inteirose retorna o numero que está faltando nessa lista. '''
    n = 0
    i = 0
   
    while i <= len(lista):
        if i not in lista:
            n = i  
    	i = i + 1      
    if n == 0:
        n = len(lista) + 1
    return n