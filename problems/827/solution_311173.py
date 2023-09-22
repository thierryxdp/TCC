def qtd_divisores(n): 
    """Função que conta quantos divisores um número, 
passado como entrada, tem.
Assinatura: int -> int
"""
    end=[]
    for i in range(1, n+1):
        if n%i==0:
            end.append(i)
    return len(end)