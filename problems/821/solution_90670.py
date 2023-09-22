def fatorial(numero):
    ''' Retorna o fatorial de um dado (numero) 
    int -> int'''
    
    resultado = numero
    while numero > 1:
        print(resultado)
        resultado = resultado * (numero -1)
        numero -= 1
        
    return resultado