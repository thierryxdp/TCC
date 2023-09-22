def filtraMultiplos(lista,n):
    '''Funcao que recebe uma lista de numeros e um numero n como entrada e retorna outra lista contendo apenas os 
    elementos da lista original divisiveis por n;
    list,int->list'''
    
    i=0
    multiplos=[]
    while i<len(lista):
        resto=lista%n
        if resto==0:
            list.append(multiplos,lista[i])
            i=i+1
            
            return multiplos