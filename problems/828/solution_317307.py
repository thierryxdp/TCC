def qtd_divisores(num):
    """Essa função conta quantos divisores um numero tem
    int->int"""
    divisores = 0
    for i in range(num):        
        if i == 0:
            i += 1        
        if num%i == 0 :
            divisores = divisores + 1            
	return divisores

###########

def primo(num):
    """Essa função confere se um numero e primo ou não
    int->bool"""
    
    # executa uma funcao q conta quantos divisores um numero tem
    # se for 1 ou 2 ele e primo
    valor = qtd_divisores(num)
        
    #primos sao divisiveis por 1 e ele mesmo
    if valor == 1:
        return True
    elif valor == 2:
        return True
    else:
        return False