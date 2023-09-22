def filtra_pares(a,b,c,d):
    
    lista1=[a,b,c,d]
    lista2=[]
    for valor in lista1:
        if valor % 2==0:
           
            lista2.append(valor)
            
    return(lista2)