def pontos_por_time(x):
    '''função que que dado resultado de jogos, retorna o
    total de ponto de um dado time
    ass: lista[lista]--> dicionario
    testes:
    '''
    dic={'Cormengo':0,'Flamínthians':0}
    if x[0][2][0]>x[0][2][1]:
         dic['Cormengo']=(dic['Cormengo'])+3
    if x[0][2][0]<x[0][2][1]:
         dic['Flamínthians']=(dic['Flamínthians'])+3
    if x[0][2][0]== x[0][2][1]:
        dic['Flamínthians']=(dic['Flamínthians'])+1
        dic['Cormengo']=(dic['Cormengo'])+1
    if x[1][2][0]>x[1][2][1]:
         dic['Cormengo']=(dic['Cormengo'])+3
    if x[1][2][0]<x[1][2][1]:
         dic['Flamínthians']=(dic['Flamínthians'])+3
    if x[1][2][0]== x[1][2][1]:
        dic['Flamínthians']=(dic['Flamínthians'])+1
        dic['Cormengo']=(dic['Cormengo'])+1
    return dic