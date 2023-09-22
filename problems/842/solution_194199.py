def pontos_por_time(lista):
    ''' Função que dada uma lista de dois elementos, onde cada 
    elemento tambem é uma lista, calcula e retorna um dicionário contendo o nome do time e o número totade pontos na fase. 
    
    lista->dicionario
   '''

    if lista[0][2][0] > lista [0][2][1] and lista [1][2][0]> lista[1][2][1]:
        return {lista [0][0]:6, lista [0][1]: 0}
    
    elif lista[0][2][0] < [0][2][1] and lista [1][2][0]< lista[1][2][1]:
         return {lista [0][0]: 0, lista [0][1]: 6}


    elif lista[0][2][0] == lista [0][2][1] and lista[0][2][0] >[0][2][1]:
         return {lista [0][0]: 4, lista [0][1]: 1}

    elif lista[0][2][0] == lista [0][2][1] and lista[0][2][0] <[0][2][1]:
         return {lista [0][0]: 1, lista [0][1]: 4}


    elif lista[0][2][0] >[0][2][1] and lista[0][2][0] == lista [0][2][1]:
            return {lista [0][0]: 4, lista [0][1]: 1}

    elif lista[0][2][0] < lista [0][2][1] and lista[0][2][0] ==[0][2][1]:
         return {lista [0][0]: 1, lista [0][1]: 4}

    else:
         return {lista [0][0]: 2, lista [0][1]: 2}