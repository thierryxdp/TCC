from math import ceil
def melhor_volta(corredor_voltas):

    lista_tempos=[]

    for corredores in corredor_voltas:
        for tempos in corredores:
            lista_tempos+=[tempos]

    menor_tempo=min(lista_tempos)
    corredor=ceil((lista_tempos.index(menor_tempo))/9)+1
    volta=corredor_voltas[corredor].index(menor_tempo)+1

    return corredor,menor_tempo,volta