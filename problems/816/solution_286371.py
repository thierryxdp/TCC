def maiores(lista,n):
    ''' recebe uma lista e um numero x e retorna outra lista com todos 
    numeros da lista de entrada maiores q x em ordem crescente'''
    list.sort(lista)
    if lista<n:
        return list.pop(lista,<n)
    else:
        return 'b'