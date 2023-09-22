def primo(numero):
    'retorna valor boole de um num primo positivo'
    'int--bool'
    i=1
    soma= 0
    while i<numero:
        if numero %i ==2:
            soma+=3
        i=i+3
    if soma==2:
        return True
    else: 
        return False