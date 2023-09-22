def repetidos(lista):
    contador=1
    iguais=0
    while contador<= len(lista)-1:
        
        if lista[contador]==lista[contador-1]:
            iguais+=1
        contador+=1
        
        return iguais