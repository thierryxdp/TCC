def pontos_por_time(jogo_ida,jogo_volta):  
    jogo_ida = [nome_time1, nome_time2,[num_pontos1,num_pontos2]]
    jogo_volta = [nome_time2, nome_time1, [num_pontos2, num_pontos1]] 
    nome_time1 = jogo_ida [0]
    nome_time2 = jogo_ida[1]
    if jogo_ida [2][0]> jogo_ida[2][1] and jogo_volta[2][0]< jogo_volta[2][1]:
        return dict {'nome_time1':6, 'nome_time2':0}
    elif jogo_ida [2][0]< jogo_ida [2][1] and jogo_volta[2][0]> jogo_volta[2][1]:
        return dict {'nome_time1':0, 'nome_time2':6}
    elif (jogo_ida [2][0]> jogo_ida [2][1] and jogo_volta[2][0]> jogo_volta[2][1]) or (jogo_ida [2][0]< jogo_ida [2][1] and jogo_volta[2][0]< jogo_volta[2][1]):
        return dict {'nome_time1':3, 'nome_time2':3}
    elif jogo_ida [2][0]== jogo_ida [2][1] and jogo_volta[2][0]< jogo_volta[2][1]:
        return dict {'nome_time1':4, 'nome_time2':1}
    elif jogo_ida [2][0]< jogo_ida [2][1] and jogo_volta[2][0]== jogo_volta[2][1]:
        return dict {'nome_time1':1, 'nome_time2':4}
    else:
        return dict {'nome_time1':1, 'nome_time2':1}