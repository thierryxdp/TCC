def soma_h(n):
    lista_num:list(range(1,n+1))
    numero=1
    
    for i in lista_num:
        numero=numero+(1/i)
        
    return round(numero,2)