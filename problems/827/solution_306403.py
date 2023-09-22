def qtd_divisores(numero):
    """ Função que conte quantos divisores um número tem"""
    
    divisores = []
    contador = 0
    
    for i in list(range(1, numero+1)):
        
        if numero % i == 0 and numero > 0:
            
            contador += 1
            
    return contador