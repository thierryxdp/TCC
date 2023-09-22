def qtd_divisores(n):
    '''Retorna o número de divisores de um número n.
    int --> int'''
    
    divisores_de_n = []

    for i in range(1,n+1):
        if n%i == 0:
            divisores_de_n.append(i)
           
    num_div = len(divisores_de_n)

    return num_div



def primo(n):
	'''A função recebe um inteiro positivo e retorna um booleano indicando se esse
	número é primo ou não.
    int --> bool'''
    
    divisores = qtd_divisores(n)
    
    if divisores == 2:
        return True
    else:
        return False