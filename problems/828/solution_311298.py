def primo(numero):
    """dado um número inteiro positivo,
verifica se este número é primo
ou não. Retorna um valor booleano"""
    divisores=0
    
    for i in range(2,numero):
        if numero % i == 0:
            if numero == i:
                divisores += 1
            else:
                return False
                
    return True