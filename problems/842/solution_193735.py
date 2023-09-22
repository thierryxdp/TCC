def pontos_por_time(lista1,lista2):
    '''funcao que recebe como entrada duas listas, denominadas lista1 e lista2, que contem informacoes e de volta, respecti 
    do numero de gols nos jogos de ida e de volta, respectivamente e retorna um dicionario que mapeia
    o numero de pontos de um time na fase
    list, list -> dicionario'''
    dicionario_saida={}
    if lista1[2][0]>lista1[2][1]:
        dicionario_saida=dicionario_saida+{lista1[0]:3,lista1[1]:0}
    if lista1[2][0]==lista1[2][1]:
        dicionario_saida=dicionario_saida+{lista1[0]:1,lista1[1]:1}
    if lista1[2][0]<lista1[2][1]:
        dicionario_saida=dicionario_saida+{lista1[0]:0,lista1[1]:3}
    if lista2[2][0]>lista2[2][1]:
        dicionario_saida=dicionario_saida+{lista1[0]:0,lista1[1]:3}
    if lista2[2][0]==lista2[2][1]:
        dicionario_saida=dicionario_saida+{lista1[0]:1,lista1[1]:1}
    if lista2[2][0]<lista2[2][1]:
        dicionario_saida=dicionario_saida+{lista1[0]:3,lista1[1]:0}
    return dicionario_saida