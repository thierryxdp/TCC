from math import ceil
def qtd_divisores(n):
    cont =0
    
    for i in range(1, ceil(n/2)+1):
        if n%i ==0:
            cont += 1
            
    return cont