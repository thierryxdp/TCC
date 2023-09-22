def primo(num):
    
    divisores = range(2, num)
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