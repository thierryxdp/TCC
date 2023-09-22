def total(lista,produtos):
    """
    Ao inserir uma lista de compras e um dicionario
    com os preços do produtos, a função calculará 
    a soma dos valores dos produtos presentes na lista.
    list, dict->float
    """
    resultado=[]
    for i in range(0,len(lista)) :
        if lista[i] in produtos:
            c=produtos[lista[i]]
            list.append(resultado,c)
            x=sum(resultado)
    return round(x,2)