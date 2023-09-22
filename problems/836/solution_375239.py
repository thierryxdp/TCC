def busca(setor, matriz):
    ''' Essa função armazena os dados de um funcionário de uma empresa 
    buscando o setor que o funcionário pertence;str,list->list'''
    lista=[]
    for linha in range(len(matriz)):
        if setor==matriz[linha][2]:
            matriz[linha].remove(setor)
            lista.append(matriz[linha])
    return lista