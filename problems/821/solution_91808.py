def fatorial(numero):

    if numero ==0: 
        return 1
        
    else: 
        fact = 1
        while(numero > 1):
            fact *= numero
            numero -= 1
        return fact