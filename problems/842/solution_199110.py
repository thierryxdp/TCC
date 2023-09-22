def pontos_por_time(lista):
    '''Funcao que receba uma lista de dois elementos,
       onde cada elemento é também uma lista, e 
       retorne um dicionario com o nome do time
       e numero total de pontos na fase
       list -> dicio
    '''
    lista=[['Cormengo','Flaminthians',[1,0]],['Flaminthians','Cormengo',[2,2]]]
    dicio= {[['Cormengo':4],['Flaminthians':1]]}
    if lista in dicio:
     return lista