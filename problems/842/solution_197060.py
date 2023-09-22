#Start your python function here
def pontos_por_time(lista):
    "Recebe um lista de dois elementos, onde cada elemento também é uma lista. Retorna o nome de cada time seguido de seus pontos na disputa; list -> dict"
    lista1 = lista[0]
    lista2 = lista[1]
    ida = lista1[2]
    volta = lista2[2]
    if(ida[0]>ida[1]):
        time1 = 3
        time2 = 0
    elif(ida[0]==ida[1]):
        time1 = 1
        time2 = 1
    else:
        time1 = 0
        time2 = 3
    if(volta[0]>volta[1]):
        time2_1 = 3
        time1_1 = 0
    elif(volta[0]==volta[1]):
        time2_1 = 1
        time1_1 = 1
    else:
        time2_1 = 0
        time1_1 = 3
    time1_T = time1+time1_1
    time2_T = time2+time2_1
    tabela = {}
    if(time1_T<time2_T):
    	tabela[lista2[0]] = time2_T
        tabela[lista1[0]] = time1_T
    else:
    	tabela[lista1[0]] = time1_T
    	tabela[lista2[0]] = time2_T
    return tabela