#Start your python function here
def pontos_por_time(x):
    '''a função recebe uma lista de dois elementos, onde os dois também sao listas
    a lista completa tem informações do numero de gols em dois jogos de futebol entre 2 times
    a função retorna um dicionario que informa o nome do time e o numero total de pontos
    os times recebem 3 pontos por vitoria e 1 ponto por empate.
    O total de pontos é a soma dos dois jogos
    assinatura: list(list,list)
    casos de teste:
    pontos_por_time([['Botameiras','Paulo da Gama',[4,0]],['Paulo da Gama','Botameiras',[2,5]]]) == {'Botameiras': 6, 'Paulo da Gama': 0}
    '''
    
    sub_lista1 = x[0]
    sub_lista2 = x[1]
    
    posiçãoL1 = sub_lista1[2]
    posiçãoL2 = sub_lista2[2]
    
    prim_elem_PL1 = posiçãoL1[0]
    seg_elem_PL1 = posiçãoL1[1]
    
    prim_elem_PL2 = posiçãoL2[0]
    seg_elem_PL2 = posiçãoL2[1]
    
    if prim_elem_PL1 > seg_elem_PL1:
        ponto1 = 3; ponto2 = 0
    elif prim_elem_PL1 == seg_elem_PL1:
        ponto1 = 1; ponto2 = 1
    elif prim_elem_PL1 < seg_elem_PL1:
        ponto1 = 0; ponto2 = 3
        
    if prim_elem_PL2 > seg_elem_PL2:
        ponto3 = 0; ponto4 = 3
    elif prim_elem_PL2 == seg_elem_PL2:
        ponto3 = 1; ponto4 = 1
    elif prim_elem_PL2 < seg_elem_PL2:
        ponto3 = 3; ponto4 = 0
        
    return {sub_lista1:(ponto1 + ponto3), sub_lista2:(ponto2 + ponto4)}