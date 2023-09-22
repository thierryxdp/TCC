def fatorial(numero): #Recebe um número
    contador = 1
    factorial = 1
    while contador <= numero:
        factorial = contador * factorial #Multiplica ele pelo seu antecessor
        contador = contador + 1
    return factorial #Retorna o número em fatorial