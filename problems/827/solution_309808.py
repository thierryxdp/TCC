def qtd_divisores(n):
    """Função que dado umm número n, calcula a quantidae de seus divisores
assinatura: int -> int
testes:
qtd_divisores(10) == 4
qtd_divisores(100) == 9
qtd_divisores(1000) == 16
"""
    divi = 0
    if(n>0):
        for i in range(1,10000):
            if(n%i==0):
                divi+=1
        return divi
    if(n<=0):
        return 0