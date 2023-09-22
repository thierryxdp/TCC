def qtd_divisores(numero):
    
    contador = 0
    
    for i in range(numero):
        divisão= numero/(i+1)
        if divisão == round(divisão):
            contador += 1
               
        
    print(contador)