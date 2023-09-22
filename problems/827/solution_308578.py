def qtd_divisores(num):
    a=0
    
    for i in range(num):
        i+=1
        if num%i==0:
            a+=1
    return a