def qtd_divisores(numero):
    '''Função que, dado um número qualquer, retorna o número de divisores desse número.
int --> int'''
    qtd_divisores = 0
    for x in range(1,numero+1):
        if numero%x == 0:
            qtd_divisores = qtd_divisores + 1
    return qtd_divisores
    
def primo(numero):
    '''Função que, dado um número inteiro positivo, verifica se ele é primo ou não (retorna True se sim ou False se não).
int --> bool'''
    if qtd_divisores(numero) == 2:
        return True
    else:
        return False