def filtraMultiplos(lista,n):
    ''' funcao que dado uma lista de numeros e um numero retorna uma outra 
    lista contendo todos os elementos da lista original que forem 
    divisiveis pelo numero ja dado. lis,int->list'''
    multiplos=[]
    indice=0
    while indice<len(lista):
         if lista[indice]%n==0:
            multiplos=multiplos+[lista[indice]]
         indice=indice+1
    return multiplos