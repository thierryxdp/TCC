def soma_h(n):
    """A função calcula e retorna o valor da soma H com n termos.
       int -> float"""
    s = 0
    for n in range(1, n+1):
        s = s + 1/n
    return round(s, 2)
#Testes:
#soma_h(4)--> 2.08
#soma_h(100)--> 5.19
#soma_h(75)--> 4.9