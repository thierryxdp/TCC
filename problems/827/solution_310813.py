def qtd_divisores(numero):
    
    contador = 0
    
    for i in range(numero):
        divisao= numero/(i+1)
        if divisao == round(divisao):
            contador += 1
               
        
    return(contador)