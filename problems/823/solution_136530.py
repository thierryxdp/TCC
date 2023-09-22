def faltante(lista):
    #formato [1,n]
    contador =0
    faltante = []
    
    while contador<len(lista):
            
        if lista[contador]-lista[contador-1]!= 1: ##diferença entre eles menor q 1
            faltante += [lista[contador]-1]
            contador+= 1
        elif lista[contador]-lista[contador-1] == 1 and lista[contador]+1 - lista[contador] == 1: ##diferença entre eles maior q 1
            faltante += [lista[contador]+1]
            contador +=1
        else:
            contador +=1
    return faltante[len(faltante)]