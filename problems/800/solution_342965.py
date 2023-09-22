def total (lista, dicio):
    ''' funcao que recebe uma lista e um dicionario e retorna o valor total dos elementos da lista que estao no dicionario;
    list, dicio-> float'''
   
    valor=0
    b=list(dict.values(dicio))
    
    for i in range(len(lista)):
        if dicio[lista[i]] in b:
            valor+= dicio[lista[i]]
    return  round(valor ,2)