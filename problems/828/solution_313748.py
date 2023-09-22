def primo(n: int):
    """ dado um número inteiro positivo, verificar se esse número é primo
    ou não e retorna um valor booleano, false: não é primo,
    true: é primo """
    
    lista = 0
    
    for numero in list(range(2, n+1)):
        if n % numero == 0:
            lista += 1
            
    if lista > 1:
        return False
    else:
        return True