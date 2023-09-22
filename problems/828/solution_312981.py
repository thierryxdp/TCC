#---------------------EXERCICIO 2---------------------

def qtd_divisores (numero):
    '''Retorna quantos numeros divisores existem
       int -> int'''
    
    if numero<=0:
        return 0
    
    divisores = 2 #por conta do 1 do próprio número
    
    for contador in range(2,(numero//2)+1):
        divisores += (numero%contador == 0)
            
    return divisores

#-----------------EXERCICIO 3------------------------

def primo (numero):
    '''Retorna se um numero é primo ou não
       int -> bool'''
    if numero<=1:
        return False
    
    divisores = qtd_divisores(numero)
    return divisores<3