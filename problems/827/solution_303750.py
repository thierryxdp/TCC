from math import ceil
def qtd_divisores(n):
    cont =1 #Considerando que n é divisor de n
    
    for i in range(1, ceil(n/2)+1): # buscando os demais divisores, caso existam
        if n%i ==0:
            cont += 1
            
    return cont