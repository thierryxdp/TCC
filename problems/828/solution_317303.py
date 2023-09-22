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
    """
    int->bool"""
    valor = qtd_divisores(num)
    
    if valor == 1:
        return True
    elif valor == 2:
        return True
    else:
        return False