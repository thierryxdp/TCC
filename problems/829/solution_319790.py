def soma_h (N):
    """Função que dado um numero inteiro N, retorna a soma 1 + 1/2 + 1/3+ 1/4+ ... + 1/N;
        int -> int."""
    numerador= 1
    denominador= 1
    lista = []
    for i in list (range (1, N+1)):
        list.append (lista, numerador/denominador)
        denominador= denominador + 1
    return round (sum (lista),2)