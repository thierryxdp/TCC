def pontos_por_time (dados):
    '''função que retorna o nome do time e quantos pontos ele fez nos dois jogos (ida e volta)'''
    lista1,lista2 = dados
    p1 = 0
    p2 = 0
    if lista1[2][0] > lista1[2][1]:
        p1 = p1 + 3
    elif lista1 [2][0] < lista1[2][1]:
        p2 = p2 + 3
    else:
        p1 = p1 + 1
        p2 = p2 + 1
        
    if lista2 [2][0] < lista2[2][1]:
        p2 = p2 + 3 
   
    elif lista2 [2][0] > lista2[2][1]:
        p1 = p1 + 3
    else:
        p1 = p1 + 1
        p2 = p2 + 1

    return {lista1 [0]:p1, lista2 [0]:p2}