#Start your python function here
def pontos_por_time(lista1):
    ponto11=lista1[1][3][1]
    ponto12=lista1[1][3][2]
    pontos1=0
    pontos2=0
    if ponto11>ponto12:
        pontos1=(pontos+3)
    elif ponto12>ponto11:
        pontos2=(pontos+3)
    elif ponto11==ponto12:
    	pontos2=(pontos+1)
        pontos1=(pontos+1)
    dic={}
    if pontos1>pontos2:
    	dic.append(pontos1)
        dic.append(lista1[1])
        return dic
    if pontos2>pontos1:
    	dic.append(pontos2)
        dic.append(lista1[2])
    	return dic