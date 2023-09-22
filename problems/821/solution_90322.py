def fatorial(numero):
    "funcao que dado um numero, calcula o fatorial dele(int)"
    lista = list(range(1,numero))
    posicao = 0
    resposta = lista[posicao]
    while posicao < len(lista):
        resposta = resposta * lista[posicao+1]
        posicao += 1
        return resposta