def qtd_divisores(n):
    d = 0
    if(n>0):
        for i in range(1, 10000):
            if(n%i == 0):
                d+=1
        return d
    else:
        return 0
    
def primo(n):
    """Dado um número inteiro e positivo, retorna se 
esse número é primo ou não. Indo pelo pensamento de que números
primos só podem ser divididos por 1 e por ele mesmo.
assinatura: int --> bool
casos de teste:
primo(1) == False
primo(2) == True
primo(4) == False
primo(47) == True
"""
    return qtd_divisores(n)==2