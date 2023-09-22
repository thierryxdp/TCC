def primo(numero):
    '''Funcao recebe um numero e verifica se ele e primo ou nao
int -> bool'''
    qtd_divisores = 0
    
    for i in range(1,numero+1):
        if (numero%i == 0):
            qtd_divisores +=1 
        
    if(qtd_divisores == 2):
        return True
    else:
        return False