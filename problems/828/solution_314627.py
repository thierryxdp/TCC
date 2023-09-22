def qtd_divisores(inteiro):
    '''Funcao recebe um numero inteiro e retorna quais sao os seus divisores inetiros
int -> list'''
    divisores = 0
    acumulador = []
    contador = 0
    
    while (len(acumulador) < inteiro):
        acumulador += [contador+1]
        contador +=1
    
    for i in acumulador:
        if (inteiro%i == 0):
            divisores += 1
            
    return divisores
def primo(numero):
    '''Funcao recebe um numero e verifica se ele e primo ou nao
int -> bool'''
    if (numero ==
    if(qtd_divisores(numero) == 2):
        return True
    else:
        return False