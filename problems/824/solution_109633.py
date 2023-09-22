def uppCons(palavra):
    lista = list(palavra)
    lista2 = list("bcdfghjklmnpqstvwxyz")
    i = 0 
    while i < len (lista):
        j=0
        while j < len (lista2):
            if lista[i] == lista2[j]:
                lista[i].upper()
            j+=1
        i+=1
    
    return palavra