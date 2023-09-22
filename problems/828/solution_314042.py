def qtd_divisores(n:int)->int:
    '''retorna a quantidade de divisores que um número (n) tem'''
    resultado = 0
    for numero in range(1,n+1):
        if(n % numero) == 0:
            resultado = resultado + 1
    return resultado

def primo(n:int)->int:
    '''retorna True se o número dado como parâmetro é primo e False se não'''
        if qtd_divisores(n) < 3:
            return True
        else:
            return False