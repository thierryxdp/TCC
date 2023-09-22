def filtraMultiplos(lista, divisor):
    """ A funçao filtraMultiplos recebe como entrada uma lista de números e um número, e retorna outra lista contendo todos os elementos da lista original que forem divisíveis por n.
            list, int --> list"""
   
    i = 0
    resultado = []
    while i<len(lista):
        if lista[i]%divisor == 0:
            resultado = resultado + [lista[i]]
        i=i+1

    return resultado

print (filtraMultiplos([1,2,3,4,5,6],2), filtraMultiplos([15],3), filtraMultiplos([7],2))