def faltante(lista):
    """recebe uma lista e verifica qual
numero está faltando de acordo com a
sequencia"""
    list.sort(lista)
    i=0
    while i < len(lista):
        novalista = list(range(1,lista[-1]+1))
        novalista = novalista + [novalista[-1]+1]
        lista1 = lista[:]
        lista1 = lista1 + [lista1[-1]+1]
        
        if list.index(lista1,lista1[-1]) == list.index(novalista,novalista[-1]):
            return lista1[-1]
        
        if lista[i] != novalista[i]:
            return novalista[i]
            
        i = i + 1