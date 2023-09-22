def pontos_por_time(lista)
'''função que recebe uma lista de dois elementos onde cada elemento é tambem uma lista com
informações sobre o número de gols em dois jogos e retorna um dicionário que retorna a quantidade
de pontos feito pelo time na fase
lista->dicionário'''
if lista[2][0]>lista[2][1]:
    pontotime1jg1=3
    pontotime2jg1=0
if lista[2][0]==lista[2][1]:
    pontotime1jg1=1
    pontotime2jg1=1
if lista[2][0]<lista[2][1]:
    pontotime1jg1=0
    pontotime2jg1=3
if lista[3][0]>lista[3][1]:
    pontotime1jg2=3
    pontotime2jg2=0
if lista[3][0]==lista[3][1]:
    pontotime1jg2=1
    pontotime2jg2=1
if lista[3][0]<lista[3][1]:
    pontotime1jg2=0
    pontotime2jg2=3
PontosNaFase={lista[0]:pontotime1jg1+pontotime1jg2,lista[1]:pontime2jg1+pontime2jg2}