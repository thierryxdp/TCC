def faltante(lista):
    """funcao que, dada uma lista com N − 1 inteiros 
    numerados de 1 a N, descobre qual numero inteiro deste 
    intervalo esta faltando;
    list -> int"""
    
    resposta = []
    numero = 1
    if lista[-1] == len(lista):
        return lista[-1] + 1
    while (numero - 1) < len(lista):
        if numero != lista[(numero-1)]:
            resposta = resposta + [numero]
            numero = numero + 1
    return resposta[0]