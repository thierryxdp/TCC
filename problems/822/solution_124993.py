#
#
#
#
def repetidos(lista):
    i=0    
    while i < len(lista):
        if lista[0]==lista[1]:
            n_vezes=1
            return n_vezes
        
        i=i+1
    return i