#Start your python function here
def pontos_por_time(lista):
'''Ex: pontos_por_time[['Cormengo', 'Flamínthians',[1,0], ['Flamínthians', 'Cormengo',[2,2]]]
 -><nome do time>, <número total de pontos>'''
	time1=0
    time2=0
	if lista[0][2][0]>lista[0][2][1]:
        time1=time1+3
    if lista[0][2][0]<lista[0][2][1]:
        time2=time+3
    if lista[0][2][0]==lista[0][2][1]:
        time1=time1+1
        time2=time2+1
    if lista[1][2][0]>lista[1][2][1]:
        time1=time1+3
    if lista[1][2][0]<lista[1][2][1]:
        time2=time2+3
    if lista[1][2][0]==ista[1][2][1]:
        time1=time1+1
        time2=time2+1
    return lista[0][0], time1, lista[0][1], time2