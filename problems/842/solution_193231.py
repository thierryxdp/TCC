def pontos_por_time(l1):
    """
    	Retorna um dicionário dizendo a quantidade de pontos 
        de determinado time na fase.
        list -> dict
    """
    if l1[0][2][0]>l1[0][2][1]:
        vencedor1=l1[0][0]
    if l1[0][2][0]<l1[0][2][1]:
        vencedor1=l1[0][1]
    if l1[0][2][0]==l1[0][2][1]:
        vencedor1='empate'
    if l1[1][2][0]>l1[1][2][1]:
        vencedor2=l1[1][0]
    if l1[1][2][0]<l1[1][2][1]:
        vencedor2=l1[1][1]
    if l1[1][2][0]==l1[1][2][1]:
        vencedor2='empate'
    if vencedor1==l1[0][0] and vencedor2==l1[0][0]:
        return {l1[0][0]:6,l1[0][1]:0}
    if vencedor1==l1[0][1] and vencedor2==l1[0][1]:
        return {l1[0][0]:0,l1[0][1]:6}
    if vencedor1=='empate' and vencedor2=='empate':
        return {l1[0][0]:2,l1[0][1]:2}
    if (vencedor1==l1[0][0] and vencedor2==l1[0][1])or(vencedor1==l1[0][1] and vencedor2==l1[0][0]):
        return {l1[0][0]:3,l1[0][1]:3}
    if (vencedor1==l1[0][0] and vencedor2=='empate')or(vencedor1=='empate' and vencedor2==l1[0][0]):
        return {l1[0][0]:4,l1[0][1]:1}
    if (vencedor1==l1[0][1] and vencedor2=='empate')or(vencedor1=='empate' and vencedor2==l1[0][1]):
        return {l1[0][0]:1,l1[0][1]:4}