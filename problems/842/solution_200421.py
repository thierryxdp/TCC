def pontos_por_time(lista1, lista2):
    '''Função que aponta a quantidade pontos de um time e sua classificação'''
    'dict(list,list) --> dict'

    lista1=([lista1[0],lista1[1],lista1[2]])
    lista2=([lista2[0],lista2[1],lista2[2]])
    #Nomes elucidativos

    lista1[0]=time1
    lista1[1]=time2
    lista1[2][0]=gols_time1_ida
    lista1[2][1]=gols_time2_ida

    # OBS:
    lista2[0]=time2
    lista2[1]=time1
    lista2[2][0]=gols_time2_volta
    lista2[2][1]=gols_time1_volta
    
    resultados={'vitoria':3,'empate':1,'derrota':0}
            
    #retornar um dicionario com nome_do_time e numero_de_pontos

    if gols_time1_ida > gols_time2_ida \
       and gols_time1_volta > gols_time2_volta:
        return #retornar um dicionario com nome_do_time e numero_de_pontos