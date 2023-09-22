def soma_h(n):
    """Função que calcula o valor da expressão proposta onde "n" é um inteiro que determina o número de termos
assinatura: int -> float
testes:
soma_h(5) == 2.28
soma_h(10) == 2.93
soma_h(100) == 5.19
"""
    soma = 0
    n2 = 1
    conta = 0
    while(conta!=n):
        soma += (1/n2)
        n2+=1
        conta+=1
    return round(soma,2)