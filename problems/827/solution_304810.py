def qtd_divisores(n):
    """Recebe um número e retorna quantos divisores esse número possui
       parâmetro de entrada:int
       parâmetro de saída:int"""
    i=1
    soma=0
    for i in range(1,n//2+1):
        if (n%i==0):
            soma=soma+1
        return soma