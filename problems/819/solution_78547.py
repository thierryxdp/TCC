#Questão 1
def filtraMultiplos(numeros, divisor):
    """Função que dada uma lista de números, retorna uma 
    outra lista com os multiplos do 'divisor'
    list, float -> list"""
    indice = 0
    listaNumeros = []
    while indice < len(numeros):
        if numeros[indice] % divisor == 0:
            list.append(listaNumeros, numeros[indice])
            indice += 1
        return listaNumeros