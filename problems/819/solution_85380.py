def filtraMultiplos(lista,n):
    multiplos=[]
    proximo=0
    
    while proximo<len(lista):
            if lista[proximo]%n==0:
            multiplos= list.append(multiplos,lista[proximo]) 
            proximo=proximo+1
            
            return multiplos