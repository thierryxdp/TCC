# Dado um número inteiro positivo n, esta função retorna True se o número for
# primo e False, caso contrário.
# int -> bool

from math import ceil
def primo(n):
    cont =0 #Considerando que n é divisor de n
    
    for i in range(2, ceil(n/2)+1): # buscando os demais divisores, caso existam
        if n%i ==0:
            cont += 1
            
    if cont ==0:
    	resp = True
    else:
    	resp = False
            
    return resp