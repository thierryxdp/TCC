def fatorial(numero):
    """função calcula o fatorial de um 
    número qualquer inteiro
    int--> int"""
    
    contador = 1  
    fatorial = numero 
    
    while contador < numero:  
        fatorial = fatorial * contador 
        contador = contador + 1  
    return fatorial