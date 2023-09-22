def busca(setor,matriz):
    """ dado um setor, busca os dados dos funcionarios que ali trabalham;str,list->list"""
    resposta=[]
    i=0
    while(i<len(matriz)):
        if setor in str.join(" ",matriz[i]):
            list.remove(setor,mariz[i])
            list.append(resposta,matriz[i])
        i+=1        
    return resposta