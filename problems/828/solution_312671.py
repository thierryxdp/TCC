def primo(numero):
    """Funcao que retorna de um numero é primo ou não, tendo como entrada 
    um numero inteiro."""
mult=0

for count in range(2,numero+1):
    if (numero % count == 0):
        return False

elif(mult==0):
    return True