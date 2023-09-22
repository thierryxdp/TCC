#Função que recebe uma tupla com 4 elementos inteiros e retorna uma nova tupla contendo apenas os elementos pares da tupla original.
# tupla -> tupla
def filtra_pares(tupla):
    pares=[]
    for valor in (tupla):
        if valor % 2 == 0:
            pares.append(valor)
    return pares