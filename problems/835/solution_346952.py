def melhor_volta(voltas):
    """Dada uma matriz com as 10 voltas de cada um dos 6 corredores, retorna uma tupla com as informacoes de quem foi a melhor volta,com qual tempo e qual volta"""
    """entrada: lista(lista)
    saida: tupla(int,float,int)"""
    
    lista = []
    rapido = []
    volta = []
    
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
        
    if list.index(lista,min(lista)) == 0 or 10 or 20 or 30 or 40 or 50:
        list.append(volta,1)
    elif list.index(lista,min(lista)) == 1 or 11 or 21 or 31 or 41 or 51:
        list.append(volta,2)
    elif list.index(lista,min(lista)) == 2 or 12 or 22 or 32 or 42 or 52:
        list.append(volta,3)
    elif list.index(lista,min(lista)) == 3 or 13 or 23 or 33 or 43 or 53:
        list.append(volta,4)
    elif list.index(lista,min(lista)) == 4 or 14 or 24 or 34 or 44 or 54:
        list.append(volta,5)
    elif list.index(lista,min(lista)) == 5 or 15 or 25 or 35 or 45 or 55:
        list.append(volta,6)
    elif list.index(lista,min(lista)) == 6 or 16 or 26 or 36 or 46 or 56:
        list.append(volta,7)
    elif list.index(lista,min(lista)) == 7 or 17 or 27 or 37 or 47 or 57:
        list.append(volta,8)
    elif list.index(lista,min(lista)) == 8 or 18 or 28 or 38 or 48 or 58:
        list.append(volta,9)
    elif list.index(lista,min(lista)) == 9 or 19 or 29 or 39 or 49 or 59:
        list.append(volta,10)
        
    return (rapido[0],min(lista),volta[0])