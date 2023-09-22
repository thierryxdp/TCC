def maiores(lista,n):
    """Recebe uma lista de números inteiros e um inteiro 'n' e 
    retorna uma nova lista com todos os números maiores que 'n'
    em ordem crescente.
    Assinatura: list -> list"""
    listafinal=[]
    list.append(lista,n)
    for x in range(len(lista)):
        if lista[x] > n:
            listafinal.append(lista[x])  
    return sorted(listafinal)