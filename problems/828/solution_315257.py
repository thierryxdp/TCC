def primo(num):
    contador = 0
    
    for numero in range(1, num+1):
        if num % numero == 0:
            contador += 1
    if contador > 2:
        return False
    else:
        return True