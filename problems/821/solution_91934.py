def fatorial(numero):
    "doc"
    acumulador = 1 
    fator = numero -1
    if numero < 1:  
        return 1 
    while numero != 0:  
        acumulador = acumulador*numero*(fator)       
        fator -= 1             
    return acumulador