def lista_pares(tupla):
    '''funcao que chama filtra_pares que recebe uma tupla com quatro elementos inteiros
    e retorna com uma tupla contendo apenas elementos pares, tupla->tupla'''
    pares =[tupla]
    for i in tupla:
        if i %2==0:
            pares +=[i]
        return tuple(pares)