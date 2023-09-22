def qtd_divisores(num):
    soma=0
    lista=[]
    for i in range(1,num+1):
        if num%i==0:
            soma+=1
            
    return soma