def filtraMultiplos(numeros:tuple,x):
    '''função que recebe uma lista de números e um número e retorna outra lista contendo todos os elementos da lista original que forem divisíveis po n: list,int->list'''
    lista=[]
    for n in numeros:
        if n % x == 0:
            list.append(lista,n)
    return lista