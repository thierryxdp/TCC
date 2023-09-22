def repetidos(lista):
    vezes=0
    i=0
    contador=0
    while i < len(lista):
        if lista[i] in lista :
            contador= contador + list.count(lista,lista[i])
            vezes=vezes+1
            
        i=i+1
        
    return vezes