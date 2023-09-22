def busca(setor,matriz):
    """ dado um setor, busca os dados dos funcionarios que ali trabalham;str,list->list"""
    resposta=[]
    i=0
    
    while(i<len(matriz)):
        if setor in str.join(" ",matriz[i]):
            list.append(resposta,matriz[i][0])
            list.append(resposta,matriz[i][1])
            list.append(resposta,matriz[i][3])
        i+=1        
    return [resposta[0:2]],[resposta[3:-1]]