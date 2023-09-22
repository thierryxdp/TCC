def filtraMultiplos(lista,n:list,int)->list:
    '''Função que retorna uma nova lista contendo os múltiplos do numero
    dado na lista anterior'''
    resposta = []
    i=0
    
    while i<len(lista):
        if (lista[i]%n)==0:
            list.append(resposta,lista[i])
        i+=1
    return resposta