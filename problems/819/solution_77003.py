def filtraMultiplos(lista:list, n:int) ->list:
    i=0
    multiplos = ['']
    
    while lista[i] <= lista[-1]:
        if lista[i]%n == 0:
        	multiplos = multiplos + lista[i]
        	i = i+1
    return multiplos