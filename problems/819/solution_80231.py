def filtraMultiplos(listaNumeros, n):
    """ Recebe como entrada uma lista de números e um número. 
    Retorna uma lista contendo todos os elementos da lista original 
    que forem divisíveis por n 
    list, int -> list """
    saida=[]
    i=0
    while i<len(listaNumeros):
        if listaNumeros[i]%n==0:
            saida+=[listaNumeros[i]]
        i+=1
    return saida