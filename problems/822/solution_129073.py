def repetidos(lista):
    cont1=0
    numero=0
    tamanho=len(lista)
    
    while cont1<tamanho:
        if cont1>0 and lista[cont1]==lista[cont1-1]:
            numero=numero+1
            
        cont1=cont1+1
        
    return numero