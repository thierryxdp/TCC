def pontos_por_time(resultado_jogo):
    '''Função que retorna a quantidade de pontos feito por dois times em uma competição.
    Recebe como parâmetro uma lista com dois elementos que também são duas listas de duas posições.
    lista--> Dicionario'''
    ponto_time_1=0
    ponto_time_2=0
    acesso_lista1= resultado_jogo[0]
    acessando_resultado_ida= acesso_lista1[2]
    acesso_lista2=resultado_jogo[1]
    acessando_resultado_volta=acesso_lista2[2]
    if( acessando_resultado_ida[0]> acessando_resultado_ida[1]):
        ponto_time_1+=3
        ponto_time_2+=0
    elif(acessando_resultado_ida[0]== acessando_resultado_ida[1]):
        ponto_time_1+=1
        ponto_time_2+=1
    else:
        ponto_time_1+=0
        ponto_time_2+=3
    if( acessando_resultado_volta[0]> acessando_resultado_volta[1]):
        ponto_time_1+=0
        ponto_time_2+=3
    elif(acessando_resultado_volta[0]< acessando_resultado_volta[1]):
         ponto_time_1+=3
         ponto_time_2+=0
    else:
        ponto_time_1+=1
        ponto_time_2+=1

    return {acesso_lista1[0]:ponto_time_1,acesso_lista1[1]:ponto_time_2}#Start your python function here