def filtraMultiplos(lista_numeros,num):
    '''Recebe como entrada uma lista de números e um número, 
    retornando uma lista com os elementos da lista original que 
    forem divisíveis pelo número
    list [int], int -> list [int]'''
    posicao=0
    lista_divisores=[]
    while posicao<len(lista_numeros):
        if lista_numeros[posicao]%num==0:
            lista_divisores=lista_divisores+[lista_numeros[posicao],]
        posicao=posicao+1
    return lista_divisores