def pontos_por_time(placar):
    "descriçao"
    if placar[0][2][0]>placar[0][2][1]:
        pc=3
        pf=0
    elif placar[0][2][0]<placar[0][2][1]:
        pc=0
        pf=3
    else:
        pc=1
        pf=1
    if placar[1][2][0]>placar[1][2][1]:
        pc=pc+0
        pf=pf+3
    elif placar[1][2][0]<placar[1][2][1]:
        pc=pc+3
        pf=pf+0
    else:
        pc=pc+1
        pf=pf+1
    d={placar[0][0]:pc, placar[0][1]:pf}
	return d#Start your python function here