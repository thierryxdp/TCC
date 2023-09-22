def primo(n):
    """dado um número inteiro positivo a função calcula se é primo ou não
    entrada->int
    retorna->bool"""
    
    for i in range(n):
        if i >1:
            resultado= n%i==0
            
    return not resultado