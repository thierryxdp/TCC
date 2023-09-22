def filtraMultiplos(numeros,numero):
    '''Dado uma lista de números, retorne uma outra lista contendo todos os elementos da lista original que forem divisíveis por n;
    list,int -> list'''
    indice=0
    numeros2=[]
    while numeros[0][indice]%numero==0:
        indice=indice+1
        list.append(numeros2,numeros[indice])
    return numeros2