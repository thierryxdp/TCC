#Start your python function heredef pontos_por_time(l):
    lista1=[]
    lista2=[]
    if l[0][2][0]>l[0][2][1]:
        list.append (lista1,3)
    if l[0][2][0]<l[0][2][1]:
        list.append (lista2,3)
    if l[0][2][0]==l[0][2][1]:
        list.append (lista1,1)
        list.append (lista2,1)
    if l[1][2][0]>l[1][2][1]:
        list.append (lista1,3)
    if l[1][2][0]<l[1][2][1]:
        list.append (lista2,3)
    if l[1][2][0]==l[1][2][1]:
        list.append (lista1,1)
        list.append (lista2,1)
        return {l[0][0]:sum(lista1),l[0][1]:sum(lista2)}