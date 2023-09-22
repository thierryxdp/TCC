#Questão 6
def faltante(listaNum):
    """Função que dada uma lista com números de 1 até N, faltando um número,
    retorne o número que falta;
    list-> int"""
    antecessor = listaNum[-1] - 1
    sucessor = 1
    while antecessor != 0:
        if sucessor in listaNum:
            sucessor += 1 
        else:
            return sucessor