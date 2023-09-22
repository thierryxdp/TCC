def uppCons(palavra):
    lista = list(palavra)
    lista2 = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z",]
    lista3 = str(lista2)
    i = 0 
    while i < len (lista):
        j=0
        while j < len (lista2):
            if lista[i] == lista2[j]:
                lista[i].upper()
            j+=1
        i+=1
    return (lista)