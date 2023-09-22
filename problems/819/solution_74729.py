def filtraMultiplos(lista,n):
    '''funcao que dado uma lista de numeros e o
    numero 'n' retorna os numeros dessa lista que 
    sao divisiveis por 'n'; list,int->list'''
    
    multiplos = []
    i = 0
    
    while i < len(lista):
        if n%lista[i]==0:
            multiplos = multiplos + [lista[i]]
        i = i +1
    return multiplos