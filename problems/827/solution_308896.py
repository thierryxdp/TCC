def qtd_divisores(num):
    
    lista=[]
    for i in range(1,num+1):
        if num%i==0:
            lista.append(num)
            
    return lista