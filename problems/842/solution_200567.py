#Stardef tabela(lista_t1,lista_t2):
def pontos_por_time

"""Função que recebe uma lista de dois elementos (time1, time2)
e retorna um dicionário""" 

Botameiras = Botameiras_t1[0]
Fluminantos = Fluminantos_t2[0]

pontuacao_t1 =sum(Botameiras_t1[1])
pontuacao_t2 =sum(Fluminantos_t2[1])

media_t1 = round((pontuacao_t1 / len(Botameiras_t1[1])),1)
media_t2 = round((pontuacao_t2 / len(Fluminantos_t2[1])),1)

times = [Botameiras,Fluminantos]

descricao_t1 = 'pontuacao total = ' + str(pontuacao_t1) + ',' + 'media' + '=' + str(media_t1)

descricao_t2 = 'pontuacao total = ' + str(pontuacao_t2) + ',' + 'media' + '=' + str(media_t2)

if pontuacao_t1 > pontuacao_t2:
time_campeao = {Botameiras:descricao_t1,Fluminantos:descricao_t2}
return time_campeao

if pontuacao_t2 > pontuacao_t1:
time_campeao = {Fluminantos:descricao_t2,Botameiras:descricao_t1}
return time_campeao

if pontuacao_t1 == pontuacao_t2:
time_campeao = {Botameiras:descricao_t1,Fluminantos:descricao_t2}
return time_campeao