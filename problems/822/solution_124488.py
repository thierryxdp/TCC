#Questão 4
def repetidos(listaNum):
    """Função que dada uma lista numérica, retorne a quantidade
    de vezes que um número é igual ao seu posterior,
    list -> int"""
    indice = 0
    igual = 0
    while indice < len(listaNum):
        if listaNum[indice] == listaNum[indice + 1]:
            igual +=1 
    indice += 1
    return igual