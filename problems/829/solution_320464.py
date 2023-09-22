def soma_h(n):
    lista_num=list(range(1,n+1))
    soma=0
    numero=1
   
    
    for i in lista_num:
        numero=numero+(1/i)
        soma=soma+numero
        
    return round(soma,2)