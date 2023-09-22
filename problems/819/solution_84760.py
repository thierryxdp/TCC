def filtraMultiplos(lista,n):
    ''' dado uma lsita e um número, retorna outra lista contendo todos os elementos da lista original que forem divisíveis pelo número
    list, int-> list'''
    Multiplos=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            Multiplos = Multiplos + [lista[i],]
        i = i+1
    return Multiplos