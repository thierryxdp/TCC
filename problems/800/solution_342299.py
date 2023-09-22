def total(lista,produtos):
    '''Dado uma lista de produtos e um dicionario
    contendo os produtos e seus respectivos preços,
    a função calculará a soma dos valores dos produtos
    presente na lista. list,dict->float'''
    resultado=[]
    for i in range(0,len(lista)) :
        if lista[i] in produtos:
            c=produtos[lista[i]]
            list.append(resultado,c)
            x=sum(resultado)
    return round(x,2)