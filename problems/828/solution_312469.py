#Solução do problema 2
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
    """Função que dado um número inteiro positivo, verifica se ele é ou
    não um número primo.
    
    Um número é considerado primo se tiver dois apenas dois divisore:
    1 e ele mesmo.
    
    Parameters:
    numero: Número que deve ser avaliado
    
    Returns:
    Retorna True se o número for primo, e False se ele não for.
    int -> bool
    """
    if qnt_divisores(numero) == 2:
        return True
    else:
        return false