#Questão 6
def faltante(listaNum):
    """Função que dada uma lista com números de 1 até N, faltando um número,
    retorne o número que falta;
    list-> int"""
    sucessor = 1
    if sucessor not in listaNum:
        sucessor += 1 
        return sucessor