def qtd_divisores(n):
    """esta funçao conta quantos divisores um número tem
    int->int"""
    lista=[]
    for numero in range(n):
        if numero==0:
            lista=[]
        else:
            if n%numero==0:
                list.append(lista,numero)
    lista1=len(lista)+1
    return lista1