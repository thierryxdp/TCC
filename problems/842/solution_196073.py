def pontos_por_time(f):
#list->dict
    l1 = f[0]
    l2 = f[1]
    """divide a lista f em l1(lista 1) e l2(lista 2)"""
    
#primeira pt

    ponto1 = l1[2]
    """Coloca o valor das pontuações da primeira lista em ponto 1"""

    if ponto1[0]>ponto1[1]:
        t1 = 3
        t2 = 0
    if ponto1[0]==ponto1[1]:
        t1 = 1
        t2 = 1
    if ponto1[0]<ponto1[1]:
        t1 = 0
        t2 = 3

    """
    Pega o valor das variáveis presentes em ponto1 e as compara para saber o resultado
    do primeiro jogo, atribuindo o valor às variáveis t1 e t2
    """
    
#segunda pt
        
    ponto2 = l2[2]
    """Coloca o valor das pontuações da segunda lista em ponto 2"""
    
    if ponto2[0]>ponto2[1]:
        t22 = 3
        t11 = 0
    if ponto2[0]==ponto2[1]:
        t22 = 1
        t11 = 1
    if ponto2[0]<ponto2[1]:
        t22 = 0
        t11 = 3

    """
    Pega o valor das variáveis presentes em ponto2 e as compara para saber o resultado
    do segundo jogo, atribuindo o valor às variáveis t11 e t22
    """

    pontos1 = t1+ t11
    pontos2 = t2+ t22

    """Soma os pontos de cada time após os dois jogos"""
    
    fase = {}
    fase[l1[0]] = pontos1
    fase[l2[0]] = pontos2
    """Cria um dicionário e coloca em ordem <nome do time> e <pontos do time>"""

    #Casos de teste
	"""
	pontos_por_time([["Macabuzinho FC", "Macaé FC", [3,2]],["Macaé FC", "Macabuzinho FC", [0,2]]]) == {'Macabuzinho FC': 6, 'Macaé FC': 0}
	pontos_por_time([["Com camisa", "Sem camisa", [10,7]],["Sem camisa", "Com camisa", [10,9]]]) == {'Com camisa': 3, 'Sem camisa': 3}
	pontos_por_time([["time1", "time2", [2,2]],["time2", "time1", [1,1]]]) == {'time1': 2, 'time2': 2}
	"""
	return fase