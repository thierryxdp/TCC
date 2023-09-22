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