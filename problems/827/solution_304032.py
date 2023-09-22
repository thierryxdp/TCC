def qtd_divisores(n):
    """esta funçao conta quantos divisores um número tem
    int->int"""
    lista=[]
    for numero in range(n):
        if numero and n==0:
            lista=[]
        if n%numero==0:
            list.append(numero,lista)
    lista1=len(lista)
    return lista1