def insere(list_numero,n):
    
    x = list.sort(list_numero)
    y=[]
    
    if list_numero[0] > n:
        x = list_numero + [n]
        return x
    
    elif list_numero[0] <= n <= list_numero[1]:
        x = list_numero + [n]
        return x
    
    elif list_numero[1] <= n <= list_numero[2]:
        x = list_numero + [n]
        return x