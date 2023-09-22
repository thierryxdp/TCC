#Recebe uma lista
#1-Precisamos ordenar essa lista
#2-Feito isso, precisamos analisar e ver qual numero falta
#3-Só um numero está faltando, logo, será o primeiro que encontrarmos
#4-Retornar esse numero
def faltante(lista:list)->int:
    """Afunção recebe uma lista e diz qual numero falta"""
    i=0
    ordenada=sorted(lista)
    listaCorreta=list(range(1, (ordenada[-1]+1)))
    retorno=0
    while i < len(lista):
        if ordenada[i] != listaCorreta[i]:
            retorno=listaCorreta[i]
            i=len(lista)
        else:
            retorn=listaCorreta[i]+1
            i+=1
    return retorno