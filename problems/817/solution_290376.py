def acima_da_media(lista): #Recebe a lista de notas
    soma_de_notas = sum(lista) #Soma todas as notas
    tamanho = len(lista) #Calcula o numero de notas
    media = soma_de_notas / tamanho #Faz a media das notas
    listamaiores = [] #Cria uma lista de notas
    for notas in lista: #Pra cada nota na lista
        if(notas > media): #Pra cada nota na lista acima da média
            list.append(listamaiores, notas) #Adiciona a nota acima da média na lista de notas
    list.sort(listamaiores) #Ordena a lista de notas
    return listamaiores #Retorna uma lista