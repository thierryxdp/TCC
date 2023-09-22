def numeros(lista):
    list.sort(lista)
    i =0
    num =0
    if lista[1] !=2:
        return 2
    
    while i <len(lista) and int(lista[i+1]) ==int(lista[i])+1:
        num =int(lista[i+1])+1
        i =i+1
  
    return num