# Função que determina o número de pontos por equipe
def pontos_por_time(placares):
    
    #variáveis de auxilio para a questão
    time1 = placares[0][0]
    time2 = placares[1][0]
    placar1 = { placares[0][0]: placares[0][2][0], placares[0][1]: placares[0][2][1] }
    placar2 = { placares[1][0]: placares[1][2][0], placares[1][1]: placares[1][2][1] }
    pontos_time1 = 0
    pontos_time2 = 0
    
    # Condição que ve quem ganhou os pontos no primeiro jogo   
    if placar1[time1] > placar1[time2]:
        pontos_time1 = pontos_time1 + 3
        
    elif placar1[time1] < placar1[time2]:
        pontos_time2 = pontos_time2 + 3
        
    else:
        pontos_time2 = pontos_time2 + 1
        pontos_time1 = pontos_time1 + 1
      
    # Condição que ve quem ganhou os pontos no segundo jogo    
    if placar2[time1] > placar2[time2]:
        pontos_time1 = pontos_time1 + 3
        
    elif placar2[time1] < placar2[time2]:
        pontos_time2 = pontos_time2 + 3
        
    else:
        pontos_time2 = pontos_time2 + 1
        pontos_time1 = pontos_time1 + 1
    
    return {time1: pontos_time1, time2: pontos_time2}


# listas para teste
lista1 = [["UFRJ", "UERJ", [1,0]],["UERJ", "UFRJ", [2,2]]]
lista2 = [["Vasmengo", "Flasco", [3,1]],["Flasco", "Vasmengo", [2,0]]]
lista3 = [["IronMan", "CapAmerica", [2,2]],["CapAmerica", "IronMan", [3,3]]]
print(pontos_por_time(lista1))
print(pontos_por_time(lista2))
print(pontos_por_time(lista3))
#Start your python function here