def pontos_por_time(j):
    ''' recebe uma lista contendo duas outras listas que contém informações sobre o número de gols de dois jogos e os nomes dos dois times que o jogaram e retorna um dicionário com o nome desses times e suas respectivas pontuações gerais'''
    j[0][0]=t1
    j[0][1]=t2
    j[0][2]=r1
    j[1][2]=r2
    if r1[0]>r1[1] and r2[1]>r2[0]:
        return {t1:6,t2:0}
    if r1[0]==r1[1] and r2[1]==r2[0]:
        return {t1:1,t2:1}
    if r1[0]<r1[1] and r2[1]<r2[0]:
        return {t1:0,t2:6}
    if (r1[0]<r1[1] and r2[1]>r2[0])or(r1[0]>r1[1] and r2[1]<r2[0]):       
        return {t1:3,t2:3}
    if (r1[0]==r1[1] and r2[1]>r2[0]) or (r1[0]>r1[1] and r2[1]==r2[0]) :
        return {t1:4,t2:1}
    if (r1[0]==r1[1] and r2[1]<r2[0])or(r1[0]<r1[1] and r2[1]==r2[0]):
        return {t1:1,t2:4}