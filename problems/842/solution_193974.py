def pontos_por_times(lista):
    ''' Função que dada uma lista de dois elementos, onde cada 
    elemento tambem é uma lista, calcula e retorna um dicionário contendo o nome do time e o número totade pontos na fase. 
    
    lista->dicionario
   '''
    
    time1= lista[2]>lista[3]== lista [2]+3 and lista[3]+0
    time2=lista[2]<lista[3]== lista[3]+3 and lista[2]+0
    empate=lista[2]==lista[3]== lista[2]+1, lista[3]+1
       
    if time1:
        return {lista[0]:time1,lista[1]:time2}
    else:
        return {lista[0]:empate,lista[1]:empate}