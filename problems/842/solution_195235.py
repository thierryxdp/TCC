def pontos_por_time(lista):
    """Funcao que dado uma lista com as informacoes de dois times, retorna a pontuacao dos dois times.:list=dicionario"""
    lista1=(lista[0])
    lista2=(lista[1])
    lista11=(lista1[0:2])
    lista21=(lista2[0:2])
    lista12=(lista1[2])
    lista22=(lista2[2])
    lista3=[]
    lista5=[]
    if lista12[0]>lista12[1]:
      lista3=[3,0]
    if lista12[0]==lista12[1]:
      lista3=[1,1]
    if lista12[0]<lista12[1]:
      lista3=[0,3]
    if lista22[0]>lista22[1]:
      lista5=[3,0]
    if lista22[0]==lista22[1]:
      lista5=[1,1]
    if lista22[0]<lista22[1]:
      lista5=[0,3]
    lista4=(lista3[0]+lista5[1]),(lista3[1]+lista5[0])
    dicionario={lista11[0]:lista4[0],lista11[1]:lista4[1]}
    return dicionario