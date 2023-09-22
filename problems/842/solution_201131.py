def pontos_por_time(lista):
    '''funcao que retorna a quantidade de pontos que os time recebem a partir do resultado das partidas'''
    time1= lista[0][0]
    time2=lista[0][1]
    gols_c_jogo1= lista[0][2][0]
    gols_f_jogo1=lista[0][2][1]
    gols_c_jogo2=lista[1][2][0]
    gols_f_jogo2=lista[1][2][1]
    if gols_c_jogo1>gols_f_jogo1:
        if gols_c_jogo2>gols_f_jogo2:
            return {time1:'6 pontos', time2:'0 pontos'}
        elif gols_c_jogo2==gols_f_jogo2:
            return {time1:'4 pontos',time2:'1 ponto'}
        elif gols_c_jogo2<gols_f_jogo2:
            return {time1:'3 pontos', time2:'3 pontos'}
        return
    elif gols_c_jogo1==gols_g_jogo1:
        if gols_c_jogo2>gols_f_jogo2:
            return {time1:'4 pontos', time2:'1 ponto'}
        elif gols_c_jogo2==gols_f_jogo2:
            return {time1:'2 pontos', time2:'2 pontos'}
        elif gols_c_jogo2<gols_f_jogo2:
            return {time1:'1 ponto', time2:'4 pontos'}
        return
    elif gols_c_jogo1<gols_f_jogo1:
        if gols_c_jogo2>gols_f_jogo2:
            return {time1:'3 pontos', time2:'3 pontos'}
        elif gols_c_jogo2==gols_f_jogo2:
            return {time1:'1 ponto', time2:'4 pontos'}
        elif gols_c_jogo2<gols_f_jogo2:
            return {time1:'0 pontos', time2:'6 pontos'}
        return
    return