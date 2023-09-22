def primo(num):
    sequencia = list(range(2,num//2+1))
    contador = 0
    
    for i in sequencia:
        if num % i == 0:
            contador += 1
            
    if contador > 0:
        return False
    
    else:
        return True