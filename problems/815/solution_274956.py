def insere(list_numero,n):
    x = list.sort(list_numero)
    if list_numero[0] =< n =< list_numero[1]:
        x = list_numero[1] = n
        return list_numero
    
    elif list_numero[1] =< n =< list_numero[2]:
        x = list_numero[2] = n
        return list_numero 
    
    else list_numero[2] =< n =< list_numero[3]:
        x = list_numero[3] = n
        return list_numero