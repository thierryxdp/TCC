def filtraMultiplos(lista,numero):
    """Recebe uma lista de numeros e um
numero, e retorna outra lista contendo todos
elementos da lista original que forem
diviseis por n
ex: ([2,4,5],2) -  [2,4]"""
    i=0
    novalista = []
    
    while i < len(lista):
        if lista[i]%numero == 0:
            novalista = novalista + [lista[i],]
        i = i + 1
    return novalista