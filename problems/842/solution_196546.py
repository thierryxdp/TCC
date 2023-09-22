def pontos_por_time ( lista ) :
   
    time1_pontos = 0
    time2_pontos = 0
    
    time1_gols = lista [ 0 ] [ 2 ] [ 0 ] # Gols feitos pelo Time 1
    time2_gols = lista [ 0 ] [ 2 ] [ 1 ] # Gols feitos pelo Time 2
    if ( time1_gols == time2_gols ) : # Empate
        time1_pontos += 1
        time2_pontos += 1
    if ( time1_gols > time2_gols ) : # Time 1 venceu
        time1_pontos += 3
    if ( time2_gols > time1_gols ) : # Time 2 venceu
        time1_pontos -= 3

    time1_gols = lista [ 1 ] [ 2 ] [ 0 ] # Gols feitos pelo Time 1
    time2_gols = lista [ 1 ] [ 2 ] [ 1 ] # Gols feitos pelo Time 2
    if ( time1_gols == time2_gols ) : # Empate
        time1_pontos += 1
        time2_pontos += 1
    if ( time1_gols > time2_gols ) : # Time 1 venceu
        time1_pontos += 3
    if ( time2_gols > time1_gols ) : # Time 2 venceu
        time1_pontos += 3

    time1_nome = lista [ 0 ] [ 0 ]  # Nome do Time 1
    time2_nome = lista [ 0 ] [ 1 ] # Nome do Time 2
    pontos = {} # Cria um dicionário vazio
    pontos [ time1_nome ] = time1_pontos # Adiciona o elemento ao dicionario [ Nome_Do_Time ] = pontos 
    pontos [ time2_nome ] = time2_pontos # Adiciona o elemento ao dicionario [ Nome_Do_Time ] = pontos 
        
    return pontos