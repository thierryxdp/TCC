#Start your python function hdef pontos_por_time ( lista ) :
   
    time1_pontos = 0
    time2_pontos = 0
    
    time1_gols = lista [ 0 ] [ 2 ] [ 0 ] # Gols feitos pelo Time a
    time2_gols = lista [ 0 ] [ 2 ] [ 1 ] # Gols feitos pelo Time b
    if ( time1_gols == time2_gols ) : # Empate
        time1_pontos += 1
        time2_pontos += 1
    if ( time1_gols > time2_gols ) : # Time 1 venceu
        time1_pontos += 3
    if ( time2_gols > time1_gols ) : # Time 2 venceu
        time2_pontos += 3

    time2_gols = lista [ 1 ] [ 2 ] [ 0 ] # Gols feitos pelo Time 1
    time1_gols = lista [ 1 ] [ 2 ] [ 1 ] # Gols feitos pelo Time 2
    if ( time1_gols == time2_gols ) : # Empate
        time1_pontos += 1
        time2_pontos += 1
    if ( time1_gols > time2_gols ) : # Time 1 venceu
        time1_pontos += 3
    if ( time2_gols > time1_gols ) : # Time 2 venceu
        time2_pontos += 3

    time1_nome = lista [ 0 ] [ 0 ]  # Nome do Time 1
    time2_nome = lista [ 0 ] [ 1 ] # Nome do Time 2
    pontos = {time2_nome:time2_pontos, time1_nome:time1_pontos} # Cria um dicionário vazio
    return pontos