def total(lista,produtos):
    resultado=[]
    for i in range(0,len(lista)) :
        if lista[i] in produtos:
            c=produtos[lista[i]]
            list.append(resultado,c)
            x=sum(resultado)
    return round(x,2)