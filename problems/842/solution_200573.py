def tabela(santasco_t1,flurminense_t2):
    
time1 = santasco_t1[4]
time2 = flurminense_t2[1]

pontuacao_t1 =sum(santasco_t1[1])
pontuacao_t2 =sum(flurminense_t2[1])

media_t1 = round((pontuacao_t1 / len(santasco_t1[1])),1)
media_t2 = round((pontuacao_t2 / len(flurminense_t2[1])),1)

times = [time1,time2]

descricao_t1 = 'pontuacao total = ' + str(pontuacao_t1) + ',' + 'media' + '=' + str(media_t1)

descricao_t2 = 'pontuacao total = ' + str(pontuacao_t2) + ',' + 'media' + '=' + str(media_t2)

if pontuacao_t1 > pontuacao_t2:
time_campeao = {time1:descricao_t1,time2:descricao_t2}
return time_campeao

if pontuacao_t2 > pontuacao_t1:
time_campeao = {time2:descricao_t2,time1:descricao_t1}
return time_campeao

if pontuacao_t1 == pontuacao_t2:
time_campeao = {time1:descricao_t1,time2:descricao_t2}
return time_campeao