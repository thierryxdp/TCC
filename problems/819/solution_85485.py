def filtraMultiplos(lista,n):
    '''funcao que dada uma lista, filtra os multiplos de um numero e retorna outra lista 
    contendo todos os elementos da lista originalque forem divisiveis pelo numero
    list,int -> list'''
    i=0
    novalista =[]
    while i< len(lista):
        if lista[i]%n==0:
            novalista.append(lista[i])
    	i=i+1
    return novalista