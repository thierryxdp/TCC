def uppCons(palavra):
    lista = list(palavra)
    lista2 = [bcdfghjklmzpqrstvwxyz]
    lista3 = list(lista2)
    i = 0 
    while i < len (lista):
        j=0
        while j < len (lista3):
            if lista[i] == lista3[j]:
                lista[i].upper()
            j+=1
        i+=1
    return (lista)