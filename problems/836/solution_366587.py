from math import factorial
def soma ():
    """funçao que retorna a soma S dada na questao tento denominador de 1! a 10! e o numerador de 10 a 1;
    entrada: none;
    saida: float."""
    soma = 0
    pos = 0
    d = range(1,11,-1)
    for elemento in range(1,11):
        soma += (d[pos]/factorial (elemento))*(-1)**(elemento+1)
        pos += 1
    return round(soma,2)