def soma_h(n): 
    contador=0
    for i in range(2,n+1):
        contador+=1/i      
    return round(contador+1,2)