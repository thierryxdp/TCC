def faltante(lista): 
    return [x for x in range(lista[0], lista[-1]+1)  
                               if x not in lista] 
print(faltante(lista))