def soma_h(n):
    """Calcula a soma de >n< termos a
partir da função e retorna esse valor.
assinatura: int --> float
casos de teste:
soma_h(1) == 1.0
soma_h(20) == 3.6
soma_h(10) == 2.93
"""
    soma = 0
    contador = 0
    num = 1
    while contador!=n:
        soma+= (1/num)
        num+= 1
        contador+=1
    return round(soma,2)