def pontos_por_time([[time1,time2,[gols_time1_ida,gols_time2_ida]],[time2,time1,[gols_time2_volta,gols_time1_volta]]]):
    """Retorna um dicionário com o nome do time e o numero de pontos na fase"""
    desempenho_time1 = {'time1':'pontos'}
    desempenho_time2 = {'time2':'pontos'}
    return desempenho_time1 + desempenho_time2