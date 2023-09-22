#Questão 6
def faltante(listaNum):
    """Função que dada uma lista com números de 1 até N, faltando um número,
    retorne o número que falta;
    list-> int"""
    sucessor = 1
    if sucessor in listaNum:
        sucessor += 1 
    elif sucessor not in listaNum:
        return sucessor