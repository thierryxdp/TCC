def filtraMultiplos(lista_numeros,numero):
    '''Função que recebe uma lista de números e um número como entrada,
    e retorna outra lista contendo todos os elementos da lista original
    que forem divisíeis por esse números; lista,int->lista'''
    i=0
    nova_lista=[]
    while i<len(lista_numeros):
        if int(lista_numeros[i])%numero == 0:
            list.append(nova_lista,lista_numeros[i])
        i+=1
    return nova_lista