def pontos_po_time(lista):
    jogo1=lista.pop(0)
    pjogo2=lista1[:1]
    jogo2=pjogo2.pop(0)
    time1=str(jogo1[0])
    time2=str(jogo1[1])
    resultado1=jogo1.pop(2)
    resultado2=jogo2.pop(2)
    total_de_pontos_mengo_rodada1=[]
    if resultado1[0]>resultado1[1]:
        x=3
    elif resultado1[0]==resultado1[1]:
        x=1
    else:
        x=0
    total_de_pontos_mengo_rodada1=int(x)
    
    total_de_pontos_mengo_rodada2=[]
    if resultado2[0]==resultado2[1]:
        y=3
    elif resultado2[0]==resultado2[1]:
        y=1
    else:
        y=0
    total_de_pontos_mengo_rodada2=int(y)
    
    total_de_pontos_corin_rodada1=[]
    if resultado1[0]<resultado1[1]:
    total_de_pontos_corin_rodada1=3
    elif resultado2[0]==resultado1[1]:
     total_de_pontos_corin_rodada1=1
    else:
    total_de_pontos_corin_rodada1=0
    
    total_de_pontos_corin_rodada2=[]
    if resultado2[0]<resultado2[1]:
    total_de_pontos_corin_rodada2=3
    elif resultado2[0]==resultado2[1]:
    total_de_pontos_corin_rodada2=1
    else:
    total_de_pontos_corin_rodada2=0
    
    total_de_pontos_corin_rodada= total_de_pontos_corin_rodada1+ total_de_pontos_corin_rodada2