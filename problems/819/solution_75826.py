def filtraMultiplos(lista,n):
    """
    Função que recebe uma lista de numeros e retorna os números dessa lista
    que são divisiveis por n
    
    list, int ---> list
    """
    nova_lista=[]
    for i in lista:
        if i%n==0:
            nova_lista.append(i)
    return nova_lista