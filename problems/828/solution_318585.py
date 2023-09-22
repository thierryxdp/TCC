def qtd_divisores(numero):
    
    divisores = 0
    
    for numeros in range(1, numero+1):
        
        if numero%numeros == 0:
            divisores = divisores + 1
    
    return divisores

def primo(numero):
    '''Função que recebe um inteiro e diz se o número é primo ou não
    por meio da função que conta a quantidade de divisores que um número
    tem
    
    int->bool'''
  
    if qtd_divisores(numero) == 2:
        return True
    
    if qtd_divisores(numero) > 2 or 1:
        return False