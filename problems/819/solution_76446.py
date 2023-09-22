def filtra_Multiplos(lista,n):
    'Função que dada uma lista e um número, retorna a lista com apenas os múltiplos do número dado. Entradas: lista[float/int], float/int. Saídas: lista[float/int].'
    #O enunciado não especifica se apenas utiliza números inteiros. 
    pos=0
    multiplos=[]
    while pos<len(lista):
        if n%lista[indice]==0:
            multiplos=multiplos+[lista[indice]]
        pos=pos+1
    return multiplos