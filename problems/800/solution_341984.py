def total(listaCompras,produtos):
    '''dada uma lista com produtos a serem comprados e 
    um dicionario com os valores dos respectivos produtos,
    essa funçao nos devolve o valor aredondado em duas casas
    decimais da compra de todos os possiveis produtos a serem
    comprados
    lista,dicionario-->float'''
    soma=0
    for i in range(len(listaCompras)):
        if listaCompras[i] in produtos:
            soma=soma+produtos[listaCompras[i]]
    return round(soma,2)