def primo(numero):
    "função que recebe um numero e retorna um booleano (primo ou não)"
    lista = list(range(1,numero+1))
    contagem = 0
    for n in lista:
        if numero%n == 0:
            contagem +=1
    return contagem <= 2