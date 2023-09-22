def filtraMultiplos(lista,n):
    '''
    Função que recebe uma lista e um número e retoruna 
    outra contendo todos os elementos da lista original divisíveis
    por n
    list, int -> list
    '''
    multiplos=[]
    p=0
    while p<len(lista):
        if lista[p]%n == 0:
            multiplos = multiplos + [lista[p]]
        p=p+1    
    return multiplos