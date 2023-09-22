def pontos_por_time(lista1,lista2):
    """lista1=[time1,time2,[golsida1,golsida2]]
    lista2=[time2,time1,[golsvolta12,golsvolta1]]
    n1,n2=nomes de time=str
    gols na ida dos times 1 e 2=int
    gols na volta dos times 1 e 2=int"""
    if((lista1[2][0]>lista1[2][1] and lista2[2][1]>lista2[2][0])):
        return {lista1[0]:6,lista1[1]:0}
    elif((lista1[2][0]>lista1[2][1] and lista2[2][1]==lista2[2][0])or(lista1[2][0]==lista1[2][1] and lista2[2][1]>lista2[2][0])):
        return {lista1[0]:4,lista1[1]:1}
    elif((lista1[2][0]>lista1[2][1] and lista2[2][1]<lista2[2][0])or(lista1[2][0]<lista1[2][1] and lista2[2][1]>lista2[2][0])):
        return {lista1[0]:3,lista1[1]:3}
    elif(lista1[2][0]==lista1[2][1] and lista2[2][1]==lista2[2][0]):
        return {lista1[0]:2,lista1[1]:2}
    elif((lista1[2][0]<lista1[2][1] and lista2[2][1]==lista2[2][0])or(lista1[2][0]==lista1[2][1] and lista2[2][1]<lista2[2][0])):
        return {lista1[0]:1,lista1[1]:4}
    else:
        return {lista1[0]:0,lista1[1]:6}