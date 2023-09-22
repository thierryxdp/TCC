def fatorial(numero):
    """Função que recebe um número e calcula o fatorial do mesmo.
    int -> int
    """
    i=0
    fatorial = 1
    num = numero
    while i < numero:
        fatorial = fatorial*num
        num= num-1
        i+=1
    return fatorial

def soma():
    """Função que calcula e retorna a seguinte soma:
    S = 10/1!-9/2!+8/3!-7/4!+...-1/10!
    
    returns:
    retorna o valor da soma S
    none -> float
    """
    soma = (10/fatorial(1)-9/fatorial(2)+8/fatorial(3)-7/fatorial(4)+6/fatorial(5))
    return round(soma,2)#Função usada no MT-7.
def fatorial(numero):
    """Função que recebe um número e calcula o fatorial do mesmo.
    int -> int
    """
    i=0
    fatorial = 1
    num = numero
    while i < numero:
        fatorial = fatorial*num
        num= num-1
        i+=1
    return fatorial

def soma():
    """Função que calcula e retorna a seguinte soma:
    S = 10/1!-9/2!+8/3!-7/4!+...-1/10!
    
    returns:
    retorna o valor da soma S
    none -> float
    """
    soma = (10/fatorial(1)-9/fatorial(2)+8/fatorial(3)-7/fatorial(4)+6/fatorial(5))
    return round(soma,2)

def soma_h(N):
    """Função que calcula e retorna o valor H com N termos, em que:
    H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N.
    
    Parameters:
    N: Número inteiro que representa a quantidade de termos de H.
    
    Returns:
    Retorna a soma H.
    int -> float|str
    """
    H = 1
    if N == 0:
        return 'erro'    
    for num in range(2,N+1):
        H = H + 1/num
    return round(H,2)