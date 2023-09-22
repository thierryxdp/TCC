def filtraMultiplos(lista,n):
    'Função que dada uma lista e um número, retorna a lista com apenas os múltiplos do número dado. Entradas: lista[float/int], float/int. Saídas: lista[float/int].'
    #O enunciado não especifica se apenas utiliza números inteiros. 
    indice=0
    multiplos=[]
    while indice<len(lista):
        if n%lista[indice]==0:
            multiplos=multiplos+[lista[indice]
        indice=indice+1
    return multiplos