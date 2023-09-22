def melhor_volta(matriz): 
    '''funçao que retorna o vencedor,o tempo e a volta em que um dos 6 corredores fez em uma das 10 voltas com base na matriz de entrada''' 
    '''list[list]->tuple''' 
    '''obs:o "+1" presente no retorno é devido ao len da lista contar a partir do 0 e n do 1'''
    lista=[] 
    vencedor=()
    for i in range(len(matriz)):
        list.append(lista,min(matriz[i]))
    tempo=min(lista) 
    compet=list.index(lista,tempo) 
    final=list.index(matriz[compet],tempo)
    vencedor=(compet+1,tempo,final+1)
    return vencedor