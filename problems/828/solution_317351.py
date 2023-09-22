def primo(numero):
    '''fun ̧c~ao que verifica se um n ́umero
qualquer  ́e primo.
int--> bool'''
    contador = 0
    for elemento in range(2, numero):
        if numero % elemento == 0:
            contador += 1
    
    if contador > 0:
        return False
    else:
        return True