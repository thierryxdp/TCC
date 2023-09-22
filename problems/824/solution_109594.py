def uppCons(palavra):
    lista = list(palavra)
    lista2 = ["b","c","d","f","g","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    i = 0 
    while i < len (lista):
        if lista[i] in lista2:
            lista[i].upper()
        i+=1
    return str(lista)