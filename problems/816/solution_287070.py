def maiores(numero,n):
    if n in numero: 
        list.sort(l_num)
        l1=list.index(numero,n)
        return numero[l1+1:]
    else: 
        list.append(numero,n)      
        list.sort(numero)
        l1=list.index(numero,n)
        return numero[l1+1:]