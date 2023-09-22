def fatorial(numero):

    if numero ==0: 
        return 1
        
    else: 
        fatorial = 1
        while(numero > 1):
            fatorial *= numero
            numero -= 1
        return fatorial