def qtd_divisores(numero):   
    soma=0
    for x in range(1,numero+1):
        if numero/x == int(numero/x):
            soma=1+soma

    return soma

def primo(numero):
    """ Essa função utiliza da função qtd_divisores da questão
    anterior para verificar se determinado número é primo ou 
    não.
    assinatura: int---> boolean"""
    return qtd_divisores(numero)==2