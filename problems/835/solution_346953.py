def melhor_volta(voltas):
    """Dada uma matriz com as 10 voltas de cada um dos 6 corredores, retorna uma tupla com as informacoes de quem foi a melhor volta,com qual tempo e qual volta"""
    """entrada: lista(lista)
    saida: tupla(int,float,int)"""
    
    lista = []
    rapido = []
    volta = []
    volta1 = [0,10,20,30,40,50]
    volta2 = [1,11,21,31,41,51]
    volta3 = [2,12,22,32,42,52]
    volta4 = [3,13,23,33,43,53]
    volta5 = [4,14,24,34,44,54]
    volta6 = [5,15,25,35,45,55]
    volta7 = [6,16,26,36,46,56]
    volta8 = [7,17,27,37,47,57]
    volta9 = [8,18,28,38,48,58]
    volta10 = [9,19,29,39,49,59]
    
    for i in range(len(voltas)):
        for j in range(len(voltas[i])):
            list.append(lista,voltas[i][j])
            
            
    if list.index(lista,min(lista)) <= 9:
        list.append(rapido,1)
    elif 9< list.index(lista,min(lista)) <= 19:
        list.append(rapido,2)
    elif 19< list.index(lista,min(lista)) <= 29:
        list.append(rapido,3)
    elif 29< list.index(lista,min(lista)) <= 39:
        list.append(rapido,4)
    elif 39< list.index(lista,min(lista)) <= 49:
        list.append(rapido,5)
    elif 49< list.index(lista,min(lista)) <= 59:
        list.append(rapido,6)
        
    if list.index(lista,min(lista)) in volta1:
        list.append(volta,1)
    elif list.index(lista,min(lista)) in volta2:
        list.append(volta,2)
    elif list.index(lista,min(lista)) in volta3:
        list.append(volta,3)
    elif list.index(lista,min(lista)) in volta4:
        list.append(volta,4)
    elif list.index(lista,min(lista)) in volta5:
        list.append(volta,5)
    elif list.index(lista,min(lista)) in volta6:
        list.append(volta,6)
    elif list.index(lista,min(lista)) in volta7:
        list.append(volta,7)
    elif list.index(lista,min(lista)) in volta8:
        list.append(volta,8)
    elif list.index(lista,min(lista)) in volta9:
        list.append(volta,9)
    elif list.index(lista,min(lista)) in volta10:
        list.append(volta,10)
        
    return (rapido[0],min(lista),volta[0])