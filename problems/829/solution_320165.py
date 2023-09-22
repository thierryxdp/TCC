#->float
def soma_h():
    "Fução que calcula a soma de um inteiro fatorial e retorna o resultado com 2 casas decimais."
    soma=0
    for denomindor in range(10,0,-1):
        fracao= 1/denominador
        soma=soma+fracao
    return round(soma,2)