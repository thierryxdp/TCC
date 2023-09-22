def fatorial(numero):
    'função que dado um número retorna o fatorial do mesmo'
    contador = 0
    numeros = list(range(1, numero + 1))
    resultado = 0
    while contador < numero:
        resultado = resultado + numero * numeros[contador]
        contador = contador + 1
    return resultado