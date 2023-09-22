def filtraMultiplos(lista,n):
    '''função que dada uma lista e um numero n, retorna outra
    outra lista contendo todos os elementos da lista original 
    que forem divisiveis por n. ent->  (list,int)   saida-> list'''
    
    multiplos = []
    indice = 0
    while indice < len(lista):
        if lista[indice]%n==0:
            list.append(multiplos,lista[indice])
        indice += 1
    return multiplos