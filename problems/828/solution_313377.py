def primo(n):
    contador = 0
    for numero in range(2, n):
        if numero % n == 0:
            contador += 1
            
        if contador == 0:
            return True
        else:
            return False