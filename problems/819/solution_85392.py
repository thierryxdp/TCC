def filtraMultiplos(listaNumeros,n):
    
    i=0
    multiplos=[]
    
    while i<len(listaNumeros):
        if listaNumeros[i]%n==0:
            multiplos=multiplos+listaNumeros[i]
            
            i=i+1
            return multiplos