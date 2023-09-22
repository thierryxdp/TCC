def maiores(lista,n):
    """Esta funcao recebe uma lista e um numero e avalia 
    quais numeros da lista são maiores que o numero fornecido
    list->list"""
    l=[]
    for i in range(len(lista)):
        if lista[i]>n:
            l.append(lista[i])