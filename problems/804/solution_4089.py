def filtra_pares(tupla):
    
    lis=[]

    for i in range(len(tupla)):
       	if tupla[i]%2 == 0:
      		lis.append(tupla[i])
        
    return tupla