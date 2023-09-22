def primo(num):
    
    divisores = list(range(3, num-1))
    resultado = 0
    
    for indice in divisores:
        if num % indice != 0:
            resultado += 1
        
        else:
            pass
    if resultado > 0:
        return False
    
    else:
        return True