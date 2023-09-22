def filtraMultiplos(lista,n):
    '''Funcao que recebe uma lista de numeros e um numero n como entrada e retorna outra lista contendo apenas os 
    elementos da lista original divisiveis por n;
    list,int->list'''
    
    i=0
    multiplos=[]
    while i<len(lista):
        if lista[i]%n == 0:
            list.append(multiplos,lista[i])
            return multiplos
        i=i+1