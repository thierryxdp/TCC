def pontos_por_time(lista):
    '''Instruções: Indique os dois elementos da lista como listas também.
    Exemplo: [[time1,time2,[gols1,gols2]],[time2,time1,[gols2,gols1]]]'''
#Definição dos times e dos resultados de ida e volta (Separando os dados de entrada)
    bloco1 = lista[0]
    bloco2 = lista[1]
    t1 = bloco1[0]
    t2 = bloco1[1]
    r1 = bloco1[2]
    r2 = bloco2[2]
    return r2