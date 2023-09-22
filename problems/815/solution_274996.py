def insere(list_numero,n):
    
    x = list.sort(list_numero)
    
    if list_numero[0] > n:
        x = [n] + [list_numero]
        return x
    
    elif list_numero[0] < n < list_numero[1]:
        x = [list_numero[0]] + [n] + [list_numero[1]]
        return x
    
    elif list_numero[1] < n:
        x = [list_numero[0]] + [list_numero[1]] + [n] + [list_numero[2]] or [list_numero] + [n] 
        return x
    elif list_numero[2] > n:
        x = [list_numero[0]] + [list_numero[1]] + [n] + [list_numero[2]] or [list_numero] + [n] 
        return x
    elif list_numero[2] < n:
        x = [list_numero] + [n]
        return x
    
    elif list_numero[3] > n:
        x = [list_numero[0]] + [list_numero[1]] + [list_numero[2]] + [n] + list_numero[3]
        return x
    else:
        x = [list_numero[0]] + [list_numero[1]] + [list_numero[2]] + [list_numero[3]] + [n]
        return x