#Questão 4
def soma_h(n):
    """Função que calcula a soma dos inversos de 1 até N;
    int -> float"""
    lista = list(range(0, n+1))
    soma = 0
    for i in lista:
        soma = soma + 1/i
    return round(soma, 2)