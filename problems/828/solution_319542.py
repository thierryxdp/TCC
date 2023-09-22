def primo(numero):
    'retorna valor boole de um num primo positivo'
    'int--bool'
    i=1
    soma=o
    while i<numero:
        if numero %i ==0:
            soma+=1
        i=i+1
    if soma==2:
        return True
    else: 
        return False