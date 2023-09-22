def repetidos(lista):
    cont=0
    num=0
    tam=len(lista)
    
    while cont<tam:
        if cont>0 and lista[cont]==lista[cont-1]:
            num=num+1
            
        cont=cont+1
        
    return num