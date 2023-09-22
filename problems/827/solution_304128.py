def qtd_divisores(x):
    """esta funçao conta quantos divisores um número tem
    int->int"""
    lista=[]
    if x<0:
        return 0
    for numero in range(x):
        if numero==0:
            lista=[]
        else:
            if x%numero==0:
                list.append(lista,numero)
    totaldiv=len(lista)+1
    return totaldiv