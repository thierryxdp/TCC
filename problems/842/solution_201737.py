def pontos_por_time(l):
    ''' dada uma lista de dois elementos, sendo cada um também uma lista. A lista completa tem informações do número de gols em dois jogos de futebol entre dois times, no seguinte formato:[[time1,time2,[goldotime1,goldotime2]],[time2,time1,[goldotime1,goldotime2]]].Retorna um dicionário com os nomes dos times e suas respecitvas pontuações;
    list->dict '''
    tabela1={lista[0][0]:6,lista[1][0]:0}
    tabela2={lista[0][0]:3,lista[1][0]:3}
    tabela3={lista[0][0]:0,lista[1][0]:6}
    tabela4={lista[0][0]:4,lista[1][0]:1}
    tabela5={lista[0][0]:1,lista[1][0]:4}
    tabela6={lista[0][0]:2,lista[1][0]:2}