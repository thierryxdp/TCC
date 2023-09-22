def qtd_divisores(n):
    divi = 0
    if(n>0):
        for i in range(1,10000):
            if(n%i==0):
                divi+=1
        return divi
    if(n<=0):
        return 0
def primo(n):
    """Função qeu informado um número inteiro n, verifica se ele é primo ou não.
assinatura: int -> bool
teste:
primo(2) == True
primo(10) == False
primo(100) == False
"""
    return qtd_divisores(n) == 2