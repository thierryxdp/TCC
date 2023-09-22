def repetidos(lista):
    contador=1
    iguais=0
    while True:
        if contador == len(lista)-1:
            break
        if lista[contador]==lista[contador-1]:
            iguais+=1
        contador+=1
        
        return iguais