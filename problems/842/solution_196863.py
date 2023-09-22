def pontos_por_time (lista):
    """funcao que dada 2 listas de informacoes sobre o numero de gols de cada time em um jogo, retorna um dicionario que tem o time como chave e a quantidade de pontos no campeonato como valor;
        list,list->dict"""
    lista_ida=lista[0]
    lista_volta=lista[2]
    pontos_time1=[]
    pontos_time2=[]
    gols_ida=lista_ida[-1]
    gols_volta=lista_volta[-1]
    if gols_ida[0]==gols_ida[1]:
        pontos_time1.append(1)
        pontos_time2.append(1)
    if gols_ida[0]>gols_ida[1]:
        pontos_time1.append(3)
        pontos_time2.append(0)
    if gols_ida[0]<gols_ida[1]:
        pontos_time2.append(3)
        pontos_time1.append(0)
    if gols_volta[0]==gols_volta[1]:
        pontos_time2.append(1)
        pontos_time1.append(1)
    if gols_volta[0]>gols_volta[1]:
        pontos_time2.append(3)
        pontos_time1.append(0)
    if gols_volta[0]<gols_volta[1]:
        pontos_time1.append(3)
        pontos_time2.append(0)  
    pontos_campeo1= (pontos_time1[0])+ (pontos_time1[1])
    pontos_campeo2= (pontos_time2[0])+ (pontos_time2[1])
    return {lista_ida[0]:pontos_campeo1, lista_volta[0]:pontos_campeo2}