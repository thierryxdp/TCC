def primo(n: int):
    lista = 0
    
    for numero in list(range(2, n+1)):
        if n % numero == 0:
            lista += 1
            
    if lista > 1:
        return False
    else:
        return True