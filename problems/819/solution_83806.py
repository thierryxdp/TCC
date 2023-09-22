def filtraMultiplos(lista,n):
    '''função que recebe uma lista e um número e retorna
    outra lista com todos os elementos da lista original que
    forem divisíveis pelo número dado.
    list>list'''
    proximo=0            
    lista_nova=[]
    while proximo<len(lista):
        if lista[proximo]%n==0:
            lista_nova=lista_nova+[lista[proximo]]
        proximo=proximo+1
    return lista_nova