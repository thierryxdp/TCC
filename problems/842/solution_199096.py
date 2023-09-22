def pontos_por_time(lista):
    '''Funcao que receba uma lista de dois elementos,
       onde cada elemento é também uma lista, e 
       retorne um dicionario com o nome do time
       e numero total de pontos na fase
       list -> dicio
    '''
    lista1=[[lista[0],lista[1]],[lista[2],lista[3]]]
    dicio={nome_time: 'Cormengo' or 'Flaminthians',total_pontos:4 or 1} 
    if lista1 in dicio:
       return dicio [lista1[0],lista1[1],lista1[2],lista1[3]]
    else:
       return dicio[lista1]