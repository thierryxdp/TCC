def porntos_por_time(lista):
	"""Função que dado dois números, que são listas, receba uma lista de dois elementos, no seguinte formato: [[<nomedotime1>,<nomedotime2>,[<golsdotime1>,<golsdotime2>]],[<nomedotime2>,<nomedotime1>,[<golsdotime2>,<golsdotime1>]]] dado que são duas partidas entre os times, resultando em um dicionário com os nomes dos times e suas referidas pontuações; list,=>dict"""
    tabela1={lista[0][0]:6,lista[1][0]:0}
    tabela2={lista[0][0]:3,lista[1][0]:3}
    tabela3={lista[0][0]:0,lista[1][0]:6}
    tabela4={lista[0][0]:4,lista[1][0]:1}
    tabela5={lista[0][0]:1,lista[1][0]:4}
    tabela6={lista[0][0]:2,lista[1][0]:2}
    if lista[0][2][0]>lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
        return tabela1
    if lista[0][2][0]>lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
        return tabela2
    if lista[0][2][0]<lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
        return tabela2
    if lista[0][2][0]<lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
        return tabela3
    if lista[0][2][0]>lista[0][2][1] and lista[1][2][0]==lista[1][2][1]:
        return tabela4
    if lista[0][2][0]==lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
        return tabela4
    if lista[0][2][0]<lista[0][2][1] and lista[1][2][0]==lista[1][2][1]:
        return tabela5
    if lista[0][2][0]==lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
        return tabela5
    if lista[0][2][0]==lista[0][2][1] and lista[1][2][0]==lista[1][2][1]:
        return tabela6