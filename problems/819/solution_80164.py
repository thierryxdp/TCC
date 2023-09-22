#Exercício_01:
''' Essa função filtra multiplos de uma lista dado um número "n", ela retorna outra lista com os números já filtrados. '''
''' list, float ---> list. '''

def filtraMultiplos(candidates, n):
    
    list_divisible = []
    i = 0
    
    while i < len(candidates):
        if (candidates[i]%n) == 0:
            list_divisible.append(candidates[i])
        i += 1
            
    return list_divisible