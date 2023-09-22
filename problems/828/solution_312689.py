# Utilizando a função divisores já criada
def qtd_divisores(numero):
    """Função que dado um número inteiro, retorna a quantidade de 
    divisores que esse número possuí.
    int -> int
    """ 
    divisor = 0
    for n in range(1,numero+1):
        if numero%n==0:
            divisor = divisor+1
    return divisor

def primo(numero):
    """Função que dado um número inteiro positivo, verifica se ele é
    ou não um número primo.
    
    Observação: Um número é primo quando tem apenas dois divisores:
    o número 1 e ele mesmo.
    
    Parameters:
    numero: É o número que será verificado.
    
    Returns:
    Retorna True se o número for primo e False se ele não for.
    int -> bool
    """
    for num in range(1, numero+1):
        if divisores(numero) == 2:
            return True
        else:
            return False