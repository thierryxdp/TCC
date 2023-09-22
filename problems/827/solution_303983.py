#int->int
def qtd_divisores(n):
    "Funçao que conta quantos divisores um número tem. Esse número será passado como entrada."
    divisores=[]
    for i in range(1,n+1):
        if n%1==0:
            divisores.append(i)
    return len(divisores)