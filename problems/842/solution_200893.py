def pontos_por_time(lista):
    ''' funcao que atraves de uma lista que contem dois elementos que sao uma lista retorna um dicionario cujos mapeamentos são nome do time e numero total de pontos
        list[list[str,str,list[int,int], list[str,str,list[int.int]]] '''
    
    if lista[0][2][0] == lista[0][2][1]:
        if lista [1][2][0] == lista [1][2][1]:
            return {'Cormengo':2, 'Flamínthias':2}
        
        elif lista [1][2][0] > lista [1][2][1]:
            return {{'Cormengo':2, 'Flamínthias':2}