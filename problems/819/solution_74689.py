def filtraMultiplos(lista,numero):
    '''recebe uma lista e um número e retorna uma lista contendo todos os elementos da lista original que forem divisíveis pelo número que foi recebido como parâmetro de entrada;lista, float->lista'''
    multiplos=[]
    indice=0
    while indice<len(lista):
        if lista[indice]%numero==0:
            list.append(multiplos, lista[indice])
            indice+=1
        else:
            indice+=1
    return multiplos