def primo(numero):
    '''funcao que verifica se o numero e primo'''
    '''int--> bool'''
    c = 0
    for elemento in range(2, numero):
        if numero % elemento == 0:
            c +=1 
    if c > 0:
        return False
    else:
        return True