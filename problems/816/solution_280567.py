def maiores(numero,n):
    x = numero[:]
    y = [n]    
    list.sort(x)
    if n>x[0]:
        (soma) =x+y
        list.sort(soma)      
        return soma[n:]
    else :
        return