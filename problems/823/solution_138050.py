def faltante(lista):
    indice = 0
    n = 0
    numeros_ate_o_momento = []
    soma = 0
    while indice < len(lista):
        numeros_ate_o_momento += [lista[indice]]
        n = len(numeros_ate_o_momento)
        soma = n*(n+1)/2
        indice += 1
    return soma - (indice + 1)